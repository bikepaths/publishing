#!/usr/bin/env python3
# NOTE: Tuner scripts are temporary sandbox tools used by the agent to adjust text before draft write.
# All formal verification and execution validation checks must be run automatically via this script or verify_blog_post.py.
import os
import sys
import subprocess

def main():
    print("--- STARTING GLOBAL SYNC ---")
    print("[1/2] Triggering remote push-sync (Server -> GitHub)...")
    
    # Trigger remote script via SSH
    ssh_cmd = ["ssh", "-p", "2323", "user0@165.232.151.110", "/usr/local/bin/bikepaths-sync"]
    res = subprocess.run(ssh_cmd)
    if res.returncode != 0:
        print("Error: Remote sync command failed.")
        sys.exit(1)
        
    print("[2/2] Pulling latest from GitHub to local repositories...")
    
    # 1. Pull /home/user0/git/publishing
    pub_dir = "/home/user0/git/publishing"
    print(f"Updating local publishing repo at {pub_dir}...")
    subprocess.run(["git", "pull"], cwd=pub_dir)
    
    # 2. Pull /home/user0/git/bikepaths if it exists
    bike_dir = "/home/user0/git/bikepaths"
    if os.path.exists(bike_dir):
        print(f"Updating local mirror repo at {bike_dir}...")
        subprocess.run(["git", "pull"], cwd=bike_dir)
        
    print("--- GLOBAL SYNC COMPLETE ---")

if __name__ == "__main__":
    main()
