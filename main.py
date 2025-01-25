import os
from rembg import remove
from PIL import Image

# Define the input directory and output directory
input_dir = "input/"
output_dir = "output/"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through all files in the input directory
for file_name in os.listdir(input_dir):
    if file_name.endswith(".jpg"):
        input_path = os.path.join(input_dir, file_name)  # Full input path
        out_path = os.path.join(output_dir, f"{file_name[:-4]}_bg.png")  # Save as PNG

        try:
            # Open the input image
            input_image = Image.open(input_path)

            # Remove the background
            output = remove(input_image)

            # Save the output image
            output.save(out_path)
            print(f"Processed {file_name} -> {out_path}")

        except Exception as e:
            print(f"An error occurred with {file_name}: {e}")
