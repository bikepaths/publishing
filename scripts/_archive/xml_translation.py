#!/usr/bin/env python3
import os
import sys
import re
import xml.etree.ElementTree as ET

def translate_markdown_to_xml(filepath):
    """
    Parses closed HTML comment tags and outputs a structured XML header payload.
    """
    if not os.path.isfile(filepath):
        print(f"Error: file {filepath} not found.")
        return None

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    metadata_regex = re.compile(r'<!--(\w+)\s+(.*?)\s+\1-->')
    metadata = dict(metadata_regex.findall(content))

    if not metadata:
        print("Error: No metadata tags detected in file.")
        return None

    root = ET.Element("post_header")
    for key, value in metadata.items():
        child = ET.SubElement(root, key)
        child.text = value

    xml_string = ET.tostring(root, encoding="utf-8").decode("utf-8")
    return xml_string

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: xml_translation.py <markdown_file>")
        sys.exit(1)
    
    xml_output = translate_markdown_to_xml(sys.argv[1])
    if xml_output:
        print(xml_output)
        sys.exit(0)
    sys.exit(1)
