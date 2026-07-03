#!/usr/bin/env python3

import argparse
import sys
import subprocess
import re
import ipaddress
import collections
import shutil
import time
from datetime import datetime

# --- Configuration ---
BLOCKED_IPS_FILE = "/home/user0/files/blocked-ips.txt"
ALLOWLIST_FILE = "/home/user0/files/allowlist-bots.txt"
LOG_ACCESS = "/var/log/apache2/bikepaths_access.log"
LOG_MAIL = "/var/log/mail.log"

# --- Colors ---
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    CYAN = '\033[0;36m'
    MAGENTA = '\033[0;35m'
    BLUE = '\033[1;34m'
    NC = '\033[0m'

# --- Helpers ---
def print_color(text, color):
    print(f"{color}{text}{Colors.NC}")

def check_root():
    import os
    if os.geteuid() != 0:
        print_color("ERROR: This script must be run as root (sudo).", Colors.RED)
        sys.exit(1)

def is_valid_ip_or_cidr(ip_str):
    try:
        ipaddress.ip_network(ip_str, strict=False)
        return True
    except ValueError:
        return False

# --- Core Classes ---

class Firewall:
    def __init__(self):
        self.blocked_networks = self.load_blocked()
        self.allowlist = self.load_allowlist()

    def load_blocked(self):
        networks = []
        try:
            with open(BLOCKED_IPS_FILE, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'): continue
                    try:
                        networks.append(ipaddress.ip_network(line, strict=False))
                    except ValueError:
                        continue
        except FileNotFoundError:
            pass
        return networks

    def load_allowlist(self):
        allowed = []
        try:
            with open(ALLOWLIST_FILE, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'): continue
                    allowed.append(line)
        except FileNotFoundError:
            pass
        return allowed

    def is_blocked(self, ip_str):
        try:
            ip = ipaddress.ip_address(ip_str)
            for net in self.blocked_networks:
                if ip in net:
                    return True
        except ValueError:
            pass
        return False

    def is_allowed(self, target):
        # 1. CIDR Check (Skip allowlist for CIDRs)
        if '/' in target:
            return False
            
        # 2. String Match against Allowlist Patterns
        # We simulate the Grep behavior: if target matches any pattern in allowlist
        for pattern in self.allowlist:
            if pattern.lower() in target.lower():
                return True
        return False

    def block_ip(self, ip_str, force=False):
        if not is_valid_ip_or_cidr(ip_str):
            print_color(f"Invalid IP/CIDR: {ip_str}", Colors.RED)
            return

        # Check Allowlist
        if self.is_allowed(ip_str):
            print_color(f"WARNING: IP {ip_str} is in your ALLOWLIST.", Colors.MAGENTA)
            if not force:
                choice = input("Block anyway? (y/N) ")
                if choice.lower() != 'y':
                    print("Skipping block.")
                    return
            else:
                print("Force block active.")

        # Add to File if not exists
        # Note: We check exact match for file appends to avoid dupes, 
        # but logic handles subnets separately.
        already_in_file = False
        try:
             with open(BLOCKED_IPS_FILE, 'r') as f:
                 lines = f.read().splitlines()
                 if ip_str in lines:
                     already_in_file = True
        except FileNotFoundError:
            pass

        if already_in_file:
            print_color(f"{ip_str} is already in tracking list.", Colors.YELLOW)
        else:
            with open(BLOCKED_IPS_FILE, 'a') as f:
                f.write(f"{ip_str}\n")
            print_color(f"Added {ip_str} to tracking list.", Colors.GREEN)
            # update internal cache
            try:
                self.blocked_networks.append(ipaddress.ip_network(ip_str, strict=False))
            except ValueError: pass

        # UFW Commands
        # Always delete first to ensure we can move it to pos 1
        subprocess.run(f"ufw delete deny from '{ip_str}'", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Insert at 1
        cmd = f"ufw insert 1 deny from '{ip_str}' to any"
        res = subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if res.returncode == 0:
            print_color(f"SUCCESS: {ip_str} blocked at position 1.", Colors.GREEN)
        else:
            print_color(f"FAILED: Could not block {ip_str} via UFW.", Colors.RED)

    def allow_ip(self, ip_str):
        if self.is_allowed(ip_str):
            print_color(f"{ip_str} is already allowed.", Colors.YELLOW)
            return
        
        with open(ALLOWLIST_FILE, 'a') as f:
            f.write(f"{ip_str}\n")
        print_color(f"Added {ip_str} to allowlist.", Colors.GREEN)
        self.allowlist.append(ip_str)

class LogScanner:
    def __init__(self, firewall):
        self.fw = firewall
        self.bad_patterns = [
            r"wp-login\.php", r"xmlrpc\.php", r"wso\.php", 
            r"/admin/", r"/backup/", r"\.env", r"wp-config\.php"
        ]

    def parse_clf_line(self, line):
        # 127.0.0.1 - - [01/Jan/2026...] "GET /..." 200 ...
        # Regex to capture: IP, Time, Method, URI, Status, Referer, UA
        # Handle cases where request is just "-" (408 timeout)
        try:
            # Standard Request: "GET /foo HTTP/1.1"
            match = re.match(r'^(\S+) \S+ \S+ \[(.*?)\] "(\S+) (\S+) \S+" (\d+) \d+ "([^"]*)" "([^"]*)"', line)
            if match:
                return {
                    'ip': match.group(1),
                    'time': match.group(2).split()[0], # Just date:time, drop timezone
                    'method': match.group(3),
                    'uri': match.group(4),
                    'status': match.group(5),
                    'referer': match.group(6),
                    'ua': match.group(7)
                }
            
            # Timeout/ Empty Request: "-" 408 ...
            match_empty = re.match(r'^(\S+) \S+ \S+ \[(.*?)\] "-" (\d+) \d+ "-" "-"', line)
            if match_empty:
                return {
                    'ip': match_empty.group(1),
                    'time': match_empty.group(2).split()[0],
                    'method': '-',
                    'uri': '-',
                    'status': match_empty.group(3),
                    'referer': '-',
                    'ua': '-'
                }

        except Exception:
            pass
        return None

    def scan_for_ip(self, ip, file_path):
        hits = []
        if not file_path: return hits
        try:
            # Using tail equivalent for speed on huge logs
            p = subprocess.Popen(['grep', ip, file_path], stdout=subprocess.PIPE, text=True)
            output, _ = p.communicate()
            if output:
                for line in output.strip().split('\n')[-15:]: # Last 15 lines
                    hits.append(line.strip())
        except Exception:
            pass
        return hits

    def print_formatted_visit(self, line):
        data = self.parse_clf_line(line)
        if not data:
            # Fallback for unparsable lines
            print(f"  {line[:100]}...") 
            return

        # Colorize Status
        s = data['status']
        c = Colors.GREEN
        if s.startswith('4') or s == '408': c = Colors.YELLOW
        if s.startswith('5'): c = Colors.RED
        if s == '200': c = Colors.GREEN
        
        # Clean Time (remove date if it's long? No, keep it for context)
        # Format: [TIME] STATUS METHOD URI
        #         UA: ...
        
        print(f"  {Colors.CYAN}[{data['time']}] {c}{s:<3}{Colors.NC} {Colors.YELLOW}{data['method']:<4}{Colors.NC} {data['uri']}")
        if data['ua'] != '-':
            # Truncate UA if huge
            ua = (data['ua'][:90] + '...') if len(data['ua']) > 90 else data['ua']
            print(f"       {Colors.MAGENTA}UA: {ua}{Colors.NC}")

    def inspect(self, ip):
        print_color(f"--- Inspecting IP: {ip} ---", Colors.YELLOW)
        bad_found = False

        # Apache
        print_color("\n[Apache Access Log - Recent Traffic]", Colors.CYAN)
        recent_logs = self.scan_for_ip(ip, LOG_ACCESS)
        if recent_logs:
            for line in recent_logs:
                # Use new formatter
                self.print_formatted_visit(line)
                
                # Check Heuristics
                for pat in self.bad_patterns:
                    if re.search(pat, line):
                        bad_found = True
            
            # Check Allowlist hint
            if any(self.fw.is_allowed(line) for line in recent_logs):
                 print_color("\nNOTICE: Activity matches Allowlist patterns (Safe Bot?).", Colors.MAGENTA)
        else:
            print("  No hits found.")

        # Mail
        print_color("\n[Mail Log - Recent Traffic]", Colors.CYAN)
        mail_hits = self.scan_for_ip(ip, LOG_MAIL)
        if mail_hits:
            for line in mail_hits: print(line)
        else:
             print("  No hits found.")

        # Alert
        if bad_found:
            print()
            print_color("[ALERT] MALICIOUS ACTIVITY DETECTED!", Colors.RED)
            print_color("Found requests for known exploit paths.", Colors.RED)

        # Whois
        print_color(f"\nWHOIS Info for {ip}:", Colors.CYAN)
        try:
            res = subprocess.run(['whois', ip], stdout=subprocess.PIPE, text=True, timeout=5)
            for line in res.stdout.split('\n'):
                if any(k in line.lower() for k in ['organization:', 'country:', 'netrange:', 'descr:']):
                    print("  " + line.strip())
        except Exception:
             print("  Whois failed.")

        return bad_found

    def scan_top_offenders(self):
        # Equivalent to 'scan_logs' in bash
        # Apache
        print_color("--- Scanning Apache Access Log ---", Colors.YELLOW)
        self._print_top_ips(LOG_ACCESS, 10, 'apache')
        
        # Mail
        print_color("\n--- Scanning Mail Log ---", Colors.YELLOW)
        self._print_top_ips(LOG_MAIL, 10, 'mail')

    def _print_top_ips(self, logfile, limit, logtype):
        counter = collections.Counter()
        try:
            with open(logfile, 'r') as f:
                for line in f:
                    ip = None
                    if logtype == 'apache':
                        parts = line.split()
                        if parts: ip = parts[0]
                    else: # mail
                        # find IP in brackets [1.2.3.4]
                        m = re.search(r'\[(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\]', line)
                        if m: ip = m.group(1)
                    
                    if ip: counter[ip] += 1
        except FileNotFoundError:
            print(f"Log {logfile} not found.")
            return

        for ip, count in counter.most_common(limit):
            status = f"{Colors.GREEN}[NEW]{Colors.NC}"
            if self.fw.is_blocked(ip):
                status = f"{Colors.RED}[BLOCKED]{Colors.NC}"
            elif self.fw.is_allowed(ip):
                 status = f"{Colors.MAGENTA}[SAFE BOT]{Colors.NC}"
            
            print(f"  {status} {count:>5} hits - {ip}")


class Reviewer:
    def __init__(self, firewall):
        self.fw = firewall
        self.scanner = LogScanner(firewall)
        self.stats_file = "/home/user0/.cron_scripts/article_stats.json"
        self.totals = self._load_stats()

    def _load_stats(self):
        import json
        try:
            with open(self.stats_file, 'r') as f:
                return json.load(f)
        except: return {}

    def _save_stats(self, daily_visitors):
        import json
        for uri, visitors in daily_visitors.items():
            existing = self.totals.get(uri, [])
            # Corrupted state fallback: if a previous buggy run saved an integer, reset it
            if not isinstance(existing, list):
                existing = []
            # Merge existing IPs with new daily visitor IPs
            self.totals[uri] = list(set(existing) | set(visitors))
        try:
            with open(self.stats_file, 'w') as f:
                json.dump(self.totals, f)
        except: pass

    def run(self):
        print_color("==================================================", Colors.BLUE)
        print_color("       BIKEPATHS.ORG - COMPLETE SITE REVIEW       ", Colors.BLUE)
        print_color("==================================================", Colors.BLUE)

        # 1. Security
        print_color("\n>>> 1. SECURITY & BOT STATUS", Colors.YELLOW)
        self.scanner.scan_top_offenders()

        # Load Log Data Once for Analytics
        print("Loading log data for analytics...")
        entries = []
        try:
            with open(LOG_ACCESS, 'r') as f:
                for line in f:
                    entry = self.scanner.parse_clf_line(line)
                    if entry: entries.append(entry)
        except FileNotFoundError:
            print("Access log not found.")
            return

        # Filter out Bots/Blocked/Local for User Analytics
        clean_entries = []
        # Support for common automated scrapers
        bot_regex = re.compile(r'bot|spider|crawler|slurp|yandex|baidu|curl|wget|python', re.I)
        current_date_str = datetime.now().strftime("%d/%b/%Y")
        
        for e in entries:
            if not e['time'].startswith(current_date_str): continue
            # 1. User-Agent Bot Check
            if bot_regex.search(e['ua']): continue
            # 2. Firewall Check
            if self.fw.is_blocked(e['ip']): continue
            # 3. Local/Production Loopback Check
            if e['ip'] in ['127.0.0.1', '::1']: continue
            
            clean_entries.append(e)

        # 2. Articles
        print_color("\n>>> 2. TOP ARTICLES (Unique Human Visitors)", Colors.YELLOW)
        article_counter = collections.Counter()
        # Track unique IP per Article to avoid counting refreshes
        article_visitors = collections.defaultdict(set)
        noisy_ext = re.compile(r'\.(css|js|xml|rss|png|jpg|jpeg|gif|ico|svg|txt|php|theme|min|webp)$', re.I)

        for e in clean_entries:
            uri = e['uri'].split('?')[0] # strip query
            if uri == '/blog/blog': uri = '/blog/' # normalize duplicate paths
            
            # EXCLUDE structural noise, directory indexes, and technical assets
            if uri == '/' or uri == '/topics' or uri == '/topics/' or noisy_ext.search(uri):
                 continue
            
            # INCLUDE Blog posts, Research PDFs, and specific content paths
            # Filtering out non-article hits like /blog/Themes/
            if ('/blog/' in uri or uri.endswith('.pdf')):
                if any(noise in uri.lower() for noise in ['/themes/', '/system/', '/feed/', '/tag/', '/category/']): 
                    continue
                article_visitors[uri].add(e['ip'])
        
        for uri, visitors in article_visitors.items():
            article_counter[uri] = len(visitors)
        
        # Persistence: Merge Daily into Total
        self._save_stats(article_visitors)

        print(f"  {'Daily':>5} | {'Total':>8} | URI")
        print(f"  {'-'*5}|{'-'*10}|{'-'*21}")
        for uri, count in article_counter.most_common(12):
            total_count = len(self.totals.get(uri, []))
            print(f"  {count:>5} | {total_count:>10} | {uri}")

        # 3. Traffic Sources
        print_color("\n>>> 3. TOP EXTERNAL SOURCES (Human Traffic Only)", Colors.YELLOW)
        ref_counter = collections.Counter()
        for e in clean_entries:
            ref = e['referer']
            # Ignore self and empty
            # Ignore self, Vercel staging noise, Internal domains, and empty referers
            internal_masks = ['bikepaths.org', 'vercel.app', 'localhost', '127.0.0.1', 'dibellasgifts.com', 'vitaminair.org', '165.232.151.110']
            if ref == '-' or any(domain in ref for domain in internal_masks):
                continue
            
            # Clean ref
            # Extract just host usually, or simple cleanup
            # visitor-sources.sh kept full URL but unique'd
            ref_counter[ref] += 1
            
        for ref, count in ref_counter.most_common(15):
            print(f"  {count:>5} - {ref}")

        # 4. Geolocation
        print_color("\n>>> 4. VISITOR GEOLOCATION", Colors.YELLOW)
        # Unique IPs
        unique_ips = set(e['ip'] for e in clean_entries)
        geo_counter = collections.Counter()
        
        # Check for geoiplookup
        has_geoip = shutil.which('geoiplookup') is not None
        
        if has_geoip:
            for ip in unique_ips:
                try:
                    res = subprocess.run(['geoiplookup', ip], stdout=subprocess.PIPE, text=True)
                    # output: GeoIP Country Edition: US, United States
                    if ":" in res.stdout:
                        country = res.stdout.split(':', 1)[1].strip().replace('GeoIP Country Edition: ', '')
                        # Clean up "IP Address not found"
                        if "not found" not in country:
                             geo_counter[country] += 1
                except Exception: pass
            
            for country, count in geo_counter.most_common(4):
                print(f"  {count:>5} - {country}")
        else:
            print_color("Error: geoiplookup not installed. Run 'sudo apt-get install geoip-bin'", Colors.RED)

        print_color("\n==================================================", Colors.BLUE)
        print_color("                 REVIEW COMPLETE                 ", Colors.BLUE)
        print_color("==================================================", Colors.BLUE)


# --- Main ---
def main():
    parser = argparse.ArgumentParser(description="Bot-Guard: Firewall & Analytics")
    parser.add_argument('ip', nargs='*', help="IPs to inspect or block")
    parser.add_argument('-f', '--force', action='store_true', help="Force block without prompt")
    parser.add_argument('-s', '--scan', action='store_true', help="Scan logs for top offenders")
    parser.add_argument('-r', '--review', action='store_true', help="Run full site review")
    parser.add_argument('-l', '--list', action='store_true', help="List blocked IPs")
    parser.add_argument('--no-color', action='store_true', help="Disable color output (good for logs/email)")
    
    args = parser.parse_args()

    if args.no_color:
        Colors.RED = ''
        Colors.GREEN = ''
        Colors.YELLOW = ''
        Colors.CYAN = ''
        Colors.MAGENTA = ''
        Colors.BLUE = ''
        Colors.NC = ''

    fw = Firewall()
    scanner = LogScanner(fw)
    reviewer = Reviewer(fw)

    if args.list:
        print_color("Currently blocked IPs/CIDRs:", Colors.YELLOW)
        with open(BLOCKED_IPS_FILE, 'r') as f:
            print(f.read())
        return

    if args.scan:
        scanner.scan_top_offenders()
        return

    if args.review:
        reviewer.run()
        return

    if not args.ip:
        parser.print_help()
        return

    # Process IPs
    for ip in args.ip:
        if args.force:
            check_root()
            fw.block_ip(ip, force=True)
        else:
            # Interactive
            is_bad = scanner.inspect(ip)
            print()
            
            if is_bad:
                 print_color("RECOMMENDATION: [B]LOCK this IP immediately.", Colors.RED)
                 prompt = f"{Colors.YELLOW}Action? [B]lock (Default), [A]llow Safe Bot, [I]gnore: {Colors.NC}"
            else:
                 prompt = f"{Colors.YELLOW}Action? [B]lock, [A]llow Safe Bot, [I]gnore (default): {Colors.NC}"
            
            choice = input(prompt).lower()
            
            if not choice and is_bad: choice = 'b' # Default block for bad
            
            if choice.startswith('b'):
                check_root()
                fw.block_ip(ip)
            elif choice.startswith('a'):
                fw.allow_ip(ip)
            else:
                print(f"Ignoring {ip}.")

if __name__ == '__main__':
    main()
