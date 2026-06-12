import os
import zipfile
import xml.etree.ElementTree as ET
import hashlib

def get_md5(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def extract_metadata(epub_path):
    ns = {
        'container': 'urn:oasis:names:tc:opendocument:xmlns:container',
        'opf': 'http://www.idpf.org/2007/opf',
        'dc': 'http://purl.org/dc/elements/1.1/'
    }
    
    metadata = {
        'path': epub_path,
        'filename': os.path.basename(epub_path),
        'size': os.path.getsize(epub_path),
        'md5': get_md5(epub_path),
        'title': 'Unknown',
        'author': 'Unknown',
        'identifier': 'Unknown',
        'language': 'Unknown',
        'files_count': 0
    }
    
    try:
        with zipfile.ZipFile(epub_path, 'r') as zip_ref:
            metadata['files_count'] = len(zip_ref.namelist())
            
            # Read container.xml to locate OPF path
            container_xml = zip_ref.read('META-INF/container.xml')
            container_root = ET.fromstring(container_xml)
            rootfile_node = container_root.find('.//container:rootfile', ns)
            if rootfile_node is None:
                return metadata
            
            opf_path = rootfile_node.attrib['full-path']
            opf_xml = zip_ref.read(opf_path)
            opf_root = ET.fromstring(opf_xml)
            
            # Extract basic DC metadata
            metadata_node = opf_root.find('opf:metadata', ns)
            if metadata_node is not None:
                title_node = metadata_node.find('dc:title', ns)
                if title_node is not None:
                    metadata['title'] = title_node.text
                    
                creator_node = metadata_node.find('dc:creator', ns)
                if creator_node is not None:
                    metadata['author'] = creator_node.text
                    
                identifier_node = metadata_node.find('dc:identifier', ns)
                if identifier_node is not None:
                    metadata['identifier'] = identifier_node.text
                    
                language_node = metadata_node.find('dc:language', ns)
                if language_node is not None:
                    metadata['language'] = language_node.text
                    
    except Exception as e:
        metadata['error'] = str(e)
        
    return metadata

if __name__ == '__main__':
    epubs = [
        '/home/user0/git/publishing/published/kdp_01_building_material_dignity.epub',
        '/home/user0/git/publishing/published/kdp_02_architecture_of_survival.epub',
        '/home/user0/git/publishing/published/the_moral_physics_of_survival.epub'
    ]
    
    print("| Book | Title | Author | Size (KB) | Files | MD5 Checksum |")
    print("| :--- | :--- | :--- | :--- | :--- | :--- |")
    for idx, epub_path in enumerate(epubs, 1):
        if not os.path.exists(epub_path):
            print(f"| Book {idx} | File not found: {epub_path} | | | | |")
            continue
        m = extract_metadata(epub_path)
        print(f"| Book {idx} | {m['title']} | {m['author']} | {m['size']/1024:.1f} | {m['files_count']} | `{m['md5']}` |")
