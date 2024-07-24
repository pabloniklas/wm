#!/usr/bin/env python3

import sys
import argparse
from PIL import Image
import numpy as np
from multiprocessing import Pool, cpu_count

WATERMARK_PATH = "/home/ttys9/watermark/logoPN.png"

def parallel_process(func, data):
    with Pool(cpu_count()) as pool:
        pool.map(func, data)

def add_watermark(image_path, watermark_path=WATERMARK_PATH):
    image = Image.open(image_path).convert("RGBA")
    watermark = Image.open(watermark_path).convert("RGBA")
    
    # Get the image dimensions
    image_width, image_height = image.size
    
    # Get the watermark dimensions
    watermark_width, watermark_height = watermark.size
    
    # Determine the maximum allowed size for the watermark
    min_side_length = min(image_width, image_height)
    max_allowed_size = min_side_length / 10
    
    # Calculate scale factor based on maximum allowed size
    if watermark_width > max_allowed_size or watermark_height > max_allowed_size:
        scale_factor = min(max_allowed_size / watermark_width, max_allowed_size / watermark_height)
        new_watermark_size = (int(watermark_width * scale_factor), int(watermark_height * scale_factor))
        watermark = watermark.resize(new_watermark_size, Image.ANTIALIAS)
    else:
        new_watermark_size = (watermark_width, watermark_height)
    
    # Update watermark dimensions
    watermark_width, watermark_height = new_watermark_size
    
    # Create an alpha mask for the watermark to make it 70% transparent
    watermark_alpha = watermark.split()[3]
    alpha = np.array(watermark_alpha)
    alpha = alpha * 0.7
    watermark_alpha = Image.fromarray(alpha.astype('uint8'))
    watermark.putalpha(watermark_alpha)

    # Position the watermark closer to the bottom right corner
    watermark_width, watermark_height = watermark.size
    position = (image_width - watermark_width - 50, image_height - watermark_height - 50)

    # Combine images
    transparent = Image.new('RGBA', (image_width, image_height), (0, 0, 0, 0))
    transparent.paste(image, (0, 0))
    transparent.paste(watermark, position, mask=watermark)
    transparent = transparent.convert("RGB")  # Remove alpha for saving in jpg format

    # Save the resulting image
    watermarked_image_path = f"watermarked_{image_path}"
    transparent.save(watermarked_image_path, "JPEG")
    print(f"Saved watermarked image as {watermarked_image_path}")

def watermark_image(image_path):
    add_watermark(image_path, WATERMARK_PATH)

def process_images(image_paths):
    from lib_cpu import parallel_process
    parallel_process(watermark_image, image_paths)

def main():
    parser = argparse.ArgumentParser(description="Watermarking program. By Pablo Niklas <pablo.niklas@gmail.com>")
    parser.add_argument("images", nargs="*", help="List of image files to watermark")
    args = parser.parse_args()
    
    if not args.images:
        parser.print_help()
        sys.exit(1)

    process_images(args.images)

if __name__ == "__main__":
    main()
