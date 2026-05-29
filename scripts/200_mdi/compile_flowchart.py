import base64
import urllib.request
import os

def main():
    mmd_path = '/home/user0/git/publishing/200_mdi/kdp/manuscript/flowchart.mmd'
    output_png = '/home/user0/git/publishing/200_mdi/kdp/handoff/framework_flowchart.png'
    output_svg = '/home/user0/git/publishing/200_mdi/kdp/handoff/framework_flowchart.svg'
    
    with open(mmd_path, 'r') as f:
        code = f.read()
    
    # Base64 encode the code
    code_bytes = code.encode('utf-8')
    base64_bytes = base64.urlsafe_b64encode(code_bytes)
    base64_string = base64_bytes.decode('ascii')
    
    # Use mermaid.ink to fetch PNG and SVG
    # Set background color to match the dark theme (1a1c1e)
    png_url = f"https://mermaid.ink/img/{base64_string}?bgColor=1a1c1e"
    svg_url = f"https://mermaid.ink/svg/{base64_string}?bgColor=1a1c1e"
    
    print(f"Fetching PNG from: {png_url}")
    try:
        req = urllib.request.Request(png_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(output_png, 'wb') as out_file:
                out_file.write(response.read())
        print(f"Successfully saved PNG to {output_png}")
    except Exception as e:
        print(f"Error fetching PNG: {e}")
        
    print(f"Fetching SVG from: {svg_url}")
    try:
        req = urllib.request.Request(svg_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(output_svg, 'wb') as out_file:
                out_file.write(response.read())
        print(f"Successfully saved SVG to {output_svg}")
    except Exception as e:
        print(f"Error fetching SVG: {e}")

if __name__ == '__main__':
    main()
