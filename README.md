# remove-bg

## Description
This project removes the background from images using the `rembg` library. It processes all `.jpg`, `.jpeg`, and `.png` images in the `input/` directory and saves the results in the `output/` directory as `.png` files.

## Requirements
- Python 3.x
- Required Python libraries:
  - `rembg`
  - `Pillow`
  - `os` (built-in)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Ameemsaeed/remove-bg.git
   cd remove-bg
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   # On Linux use:
   source venv/bin/activate
   # On Windows use:
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Place images inside the `input/` directory.
2. Run the script:
   ```sh
   python main.py
   ```
3. Processed images will be saved in the `output/` directory with `_bg.png` suffix.

## Example
**Before:** `input/example.jpg`
**After:** `output/example_bg.png`

## Notes
- The script processes only `.jpg`, `.jpeg`, and `.png` images.
- The output images are stored in PNG format to preserve transparency.
