#!/usr/bin/env python3
import os
import requests
import json
import argparse
import sys
import re

# Configuration
MANIFEST_PATH = "../manifests/multimodal_deployment_manifest.json"
OUTPUT_DIR = "../audio_outputs"
DEFAULT_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "pNInz6obbfdqIeCQ5oTs") # Default Authority Voice
API_KEY = os.getenv("ELEVENLABS_API_KEY")

def clean_markdown(text):
    """Strip markdown formatting and instructions for the narrator."""
    # Isolate only the dialogue by removing everything before the first episode marker
    episode_split = re.split(r'##\s*Episode\s*1', text, maxsplit=1, flags=re.IGNORECASE)
    if len(episode_split) > 1:
        text = episode_split[1]
        
    # Remove metadata/headers if any
    text = re.sub(r'^#.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^##.*$', '', text, flags=re.MULTILINE)
    
    # Remove NARRATOR tags and ambient sound instructions
    text = re.sub(r'\*\*\[.*?\]\*\*', '', text, flags=re.DOTALL)
    text = re.sub(r'\*\*NARRATOR:\*\*', '', text)
    
    # Remove markdown bold/italic
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    
    # Remove separators
    text = re.sub(r'^---$', '', text, flags=re.MULTILINE)
    
    # Clean up empty lines
    text = re.sub(r'\n{3,}', '\n\n', text).strip()
    return text

def generate_audio(text, output_path, voice_id):
    if not API_KEY:
        print("Error: ELEVENLABS_API_KEY environment variable not set.")
        sys.exit(1)
        
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": API_KEY
    }
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.8,
            "similarity_boost": 0.75,
            "style": 0.0,
            "use_speaker_boost": True
        }
    }
    
    print(f"Generating audio for {os.path.basename(output_path)}...")
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"✨ Successfully saved to {output_path}")
    else:
        print(f"❌ Error {response.status_code}: {response.text}")

def main():
    parser = argparse.ArgumentParser(description="Generate OVP audio from markdown scripts using ElevenLabs.")
    parser.add_argument("--dry-run", action="store_true", help="Print parsed text without calling API")
    parser.add_argument("--track", type=int, help="Specify a single track ID to generate")
    args = parser.parse_args()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    manifest_abs = os.path.normpath(os.path.join(script_dir, MANIFEST_PATH))
    out_abs = os.path.normpath(os.path.join(script_dir, OUTPUT_DIR))
    
    os.makedirs(out_abs, exist_ok=True)
    
    with open(manifest_abs, 'r') as f:
        manifest = json.load(f)
        
    for module in manifest.get("modules", []):
        track_id = module.get("track_id")
        if args.track and track_id != args.track:
            continue
            
        script_path = module.get("script_path")
        if not script_path:
            continue
            
        # script_path is relative to manifest directory
        script_abs = os.path.normpath(os.path.join(os.path.dirname(manifest_abs), script_path))
        
        if not os.path.exists(script_abs):
            print(f"Warning: Script not found at {script_abs}")
            continue
            
        with open(script_abs, 'r') as f:
            raw_text = f.read()
            
        clean_text = clean_markdown(raw_text)
        
        if args.dry_run:
            print(f"\n=== DRY RUN: Track {track_id} ===")
            print(clean_text[:300] + "...\n")
            continue
            
        out_file = os.path.join(out_abs, f"track_{track_id}_audio.mp3")
        generate_audio(clean_text, out_file, DEFAULT_VOICE_ID)

if __name__ == "__main__":
    main()
