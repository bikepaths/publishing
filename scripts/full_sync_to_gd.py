import json
import subprocess
import os
import mimetypes

ROOT_FOLDER_ID = "1_el6GWYwn0cWxHSev9eNmYbfhH4Mzig7"

def get_mime_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    if file_path.endswith('.md'): return 'text/markdown'
    if file_path.endswith('.epub'): return 'application/epub+zip'
    return mime_type or 'application/octet-stream'

def ensure_folder(parent_id, folder_name):
    params = {"q": f"'{parent_id}' in parents and name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false", "fields": "files(id)"}
    cmd = ["gws", "drive", "files", "list", "--params", json.dumps(params), "--format", "json"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    data = json.loads(res.stdout)
    if data.get("files"):
        return data["files"][0]["id"]
    else:
        create_params = {"name": folder_name, "parents": [parent_id], "mimeType": "application/vnd.google-apps.folder"}
        cmd = ["gws", "drive", "files", "create", "--json", json.dumps(create_params), "--format", "json"]
        res = subprocess.run(cmd, capture_output=True, text=True)
        return json.loads(res.stdout)["id"]

def upload_or_update(parent_id, file_name, local_path):
    mime_type = get_mime_type(local_path)
    # Check if file exists
    params = {"q": f"'{parent_id}' in parents and name = '{file_name}' and trashed = false", "fields": "files(id)"}
    cmd = ["gws", "drive", "files", "list", "--params", json.dumps(params), "--format", "json"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    data = json.loads(res.stdout)
    
    if data.get("files"):
        file_id = data["files"][0]["id"]
        # Update existing file
        cmd = ["gws", "drive", "files", "update", "--params", json.dumps({"fileId": file_id}), "--upload", local_path, "--upload-content-type", mime_type]
        subprocess.run(cmd)
        print(f"Updated: {file_name}")
    else:
        # Create new file
        create_params = {"name": file_name, "parents": [parent_id]}
        cmd = ["gws", "drive", "files", "create", "--json", json.dumps(create_params), "--upload", local_path, "--upload-content-type", mime_type]
        subprocess.run(cmd)
        print(f"Created: {file_name}")

def sync_recursive(local_root, parent_id):
    for item in os.listdir(local_root):
        if item == '.git': continue
        local_path = os.path.join(local_root, item)
        if os.path.isdir(local_path):
            folder_id = ensure_folder(parent_id, item)
            sync_recursive(local_path, folder_id)
        else:
            upload_or_update(parent_id, item, local_path)

sync_recursive("publishing_repo", ROOT_FOLDER_ID)
