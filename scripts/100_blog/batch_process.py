#!/usr/bin/env python3
"""
Batch Execution Protocol
Automates mass ingestion, validation, and deployment of pipeline artifacts.
"""
import os
import sys
import glob
import subprocess
import argparse

def execute_batch(directory, deploy=False):
    if not os.path.isdir(directory):
        print(f"[ERROR] Invalid directory: {directory}")
        sys.exit(1)
    
    files = glob.glob(os.path.join(directory, "*.md"))
    print(f"[INFO] Found {len(files)} target files in {directory}.")
    
    if len(files) == 0:
        print("\n[BATCH] No local factoids found. Initiating remote extraction (--prepare-next)...")
        prep_cmd = ["python3", "scripts/100_blog/refactor_oldposts.py", "--prepare-next"]
        prep_res = subprocess.run(prep_cmd, capture_output=True, text=True)
        
        if prep_res.returncode != 0:
            print("[FAIL] Remote extraction failed.")
            print(prep_res.stderr)
            sys.exit(1)
            
        for line in prep_res.stdout.splitlines():
            if line.startswith("Factoid created:"):
                factoid_path = line.split(":", 1)[1].strip()
                files.append(factoid_path)
                break
                
        if len(files) == 0:
            print("[FAIL] Could not identify prepared factoid.")
            sys.exit(1)
    
    success_count = 0
    fail_count = 0
    
    for file_path in files:
        print(f"\n[BATCH] Processing factoid: {os.path.basename(file_path)}")
        
        draft_cmd = ["python3", "scripts/100_blog/refactor_oldposts.py", "--draft", file_path]
        result = subprocess.run(draft_cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"[FAIL] Draft generation failed for {os.path.basename(file_path)}")
            print(result.stderr)
            fail_count += 1
            continue
            
        draft_path = None
        for line in result.stdout.splitlines():
            if line.startswith("Draft generated:"):
                draft_path = line.split(":", 1)[1].strip()
                break
                
        if not draft_path or not os.path.exists(draft_path):
            print(f"[FAIL] Could not locate generated draft for {os.path.basename(file_path)}")
            fail_count += 1
            continue
            
        print(f"[PASS] Draft ready: {draft_path}")
        
        if deploy:
            resp = input(f"\n[ACTION REQUIRED] Autonomous narrative synthesis complete at {draft_path}.\nSysop: Review generated draft.\nApprove deployment to live server? (y/N): ")
            if resp.strip().lower() != 'y':
                print("[SKIP] Deployment skipped by Sysop.")
                continue
                
            deploy_cmd = ["python3", "scripts/100_blog/refactor_oldposts.py", "--deploy", draft_path]
            deploy_result = subprocess.run(deploy_cmd)
            
            if deploy_result.returncode == 0:
                success_count += 1
            else:
                fail_count += 1
        else:
            success_count += 1
            
    print(f"\n[BATCH SUMMARY] Total: {len(files)} | Success: {success_count} | Failed: {fail_count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch Pipeline Execution Protocol")
    parser.add_argument("directory", help="Target directory containing markdown files")
    parser.add_argument("--deploy", action="store_true", help="Execute remote server synchronization after processing")
    args = parser.parse_args()
    
    execute_batch(args.directory, args.deploy)
