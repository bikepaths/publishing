import os
import sys
from PIL import Image, ImageStat

def analyze_visuals(path):
    if not os.path.exists(path):
        print(f"Error: File not found: {path}")
        sys.exit(1)
    
    with Image.open(path) as img:
        img_gray = img.convert('L')
        stat = ImageStat.Stat(img_gray)
        mean_brightness = stat.mean[0]
        std_deviation = stat.stddev[0]
        
        img_rgb = img.convert('RGB')
        stat_rgb = ImageStat.Stat(img_rgb)
        r_mean, g_mean, b_mean = stat_rgb.mean
        
        print(f"=== Visual Analysis: {os.path.basename(path)} ===")
        print(f"  Dimensions:   {img.width} x {img.height} pixels")
        print(f"  Aspect Ratio: {img.width / img.height:.4f}")
        print(f"  Mean Brightness (0-255): {mean_brightness:.2f}")
        print(f"  Contrast (Std Dev):      {std_deviation:.2f}")
        print(f"  Color Channel Averages:")
        print(f"    Red:   {r_mean:.2f}")
        print(f"    Green: {g_mean:.2f}")
        print(f"    Blue:  {b_mean:.2f}")
        
        # Validation checks
        if img.width < 1000 or img.height < 1000:
            print("  Warning: Resolution is low for high-quality production.")
            
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 analyze_visuals.py <path_to_image>")
        sys.exit(1)
    analyze_visuals(sys.argv[1])
