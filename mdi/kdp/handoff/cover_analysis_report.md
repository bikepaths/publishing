# Cover Image Visual and Technical Analysis

An audit of the cover files in `mdi/kdp/handoff/` (`cover-image.png` and `cover.jpg`) was performed to evaluate print and eBook compliance.

## 1. Technical Properties

* **Dimensions**: 1024 x 1536 pixels
* **Aspect Ratio**: 2:3 (0.6667)
* **Color Space**: RGB
* **DPI**: Not specified (defaults to standard screen resolution, 72/96 DPI)

## 2. Visual Characterization

* **Brightness**: 76.06 / 255. The image is low-key and dark, supporting a serious, strategic narrative tone.
* **Contrast**: 56.11. Robust contrast indicates that foreground text and key shapes will be clearly distinguishable from the dark background.
* **Color Distribution**: Red (84.19), Green (74.86), Blue (60.95). A warm, dark-toned color balance with minimal saturation.

## 3. Production Compliance

### eBook (Kindle KDP)
* **Status**: **PASS**
* **Details**: KDP requires a minimum of 1000 x 625 pixels. The 1024 x 1536 dimensions exceed this minimum, and the 2:3 aspect ratio is fully compatible.

### Print (Paperback/Hardcover)
* **Status**: **FAIL (Low Resolution)**
* **Details**: High-quality print output requires 300 DPI. At 300 DPI, the current dimensions (1024 x 1536) yield a maximum print size of **3.4" x 5.1"**. For a standard **6" x 9"** trim size, the front cover image must be at least **1800 x 2700 pixels** (excluding bleed). Attempting to upload the current image for print will trigger KDP low-resolution warnings and cause blurred print output.
