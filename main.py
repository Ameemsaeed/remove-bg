import os
from rembg import remove
from PIL import Image

# Define the input and output directories
input_dir = "input/"
output_dir = "output/"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Loop through all files in the input directory
for file_name in os.listdir(input_dir):
    if file_name.lower().endswith((".jpg", ".jpeg", ".png")):  # Support multiple formats
        input_path = os.path.join(input_dir, file_name)  # Full input path
        output_path = os.path.join(output_dir, f"{os.path.splitext(file_name)[0]}_bg.png")  # Save as PNG

        try:
            # Open and process the image
            with Image.open(input_path) as input_image:
                output = remove(input_image)
                output.save(output_path, format="PNG")
                print(f"Processed: {file_name} -> {output_path}")

        except Exception as e:
            print(f"An error occurred with {file_name}: {e}")
