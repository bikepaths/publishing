#!/usr/bin/env python3
# Generate a standard v1 .torrent file and output its Info Hash
import os
import sys
import hashlib

def bencode(data):
    if isinstance(data, bytes):
        return b'%d:%b' % (len(data), data)
    elif isinstance(data, str):
        return b'%d:%b' % (len(data), data.encode('utf-8'))
    elif isinstance(data, int):
        return b'i%de' % data
    elif isinstance(data, list):
        return b'l%be' % b''.join(bencode(x) for x in data)
    elif isinstance(data, dict):
        encoded_keys = []
        for k, v in data.items():
            encoded_keys.append((k.encode('utf-8') if isinstance(k, str) else k, bencode(v)))
        encoded_keys.sort()
        return b'd%be' % b''.join(k + v for k, v in encoded_keys)
    raise TypeError('Unsupported type: %s' % type(data))

def create_torrent(file_path, trackers, output_torrent_path, piece_size=262144):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file not found: {file_path}")
    
    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)
    
    pieces = []
    with open(file_path, 'rb') as f:
        while True:
            piece = f.read(piece_size)
            if not piece:
                break
            pieces.append(hashlib.sha1(piece).digest())
    
    info = {
        'name': file_name,
        'piece length': piece_size,
        'pieces': b''.join(pieces),
        'length': file_size
    }
    
    bencoded_info = bencode(info)
    info_hash = hashlib.sha1(bencoded_info).hexdigest()
    
    torrent_data = {
        'announce': trackers[0],
        'announce-list': [[t] for t in trackers],
        'info': info
    }
    
    with open(output_torrent_path, 'wb') as f:
        f.write(bencode(torrent_data))
        
    return info_hash

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python create_torrent.py <file_path> <output_torrent_path>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_torrent = sys.argv[2]
    
    public_trackers = [
        'udp://tracker.opentrackr.org:1337/announce',
        'udp://open.stealth.si:80/announce',
        'udp://tracker.coppersurfer.tk:6969/announce'
    ]
    
    try:
        hash_val = create_torrent(input_file, public_trackers, output_torrent)
        print(f"Torrent successfully created: {output_torrent}")
        print(f"Info Hash: {hash_val}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
