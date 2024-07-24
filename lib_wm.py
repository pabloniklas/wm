from PIL import Image
import numpy as np

WATERMARK_PATH = "logoPN.png"

def add_watermark(image_path, watermark_path=WATERMARK_PATH):
    image = Image.open(image_path).convert("RGBA")
    watermark = Image.open(watermark_path).convert("RGBA")
    
    # Resize watermark to fit the image
    image_width, image_height = image.size
    watermark_width, watermark_height = watermark.size
    scale_factor = min(image_width / (2 * watermark_width), image_height / (2 * watermark_height))
    new_watermark_size = (int(watermark_width * scale_factor), int(watermark_height * scale_factor))
    watermark = watermark.resize(new_watermark_size, Image.ANTIALIAS)

    # Create an alpha mask for the watermark to make it 70% transparent
    watermark_alpha = watermark.split()[3]
    alpha = np.array(watermark_alpha)
    alpha = alpha * 0.7
    watermark_alpha = Image.fromarray(alpha.astype('uint8'))
    watermark.putalpha(watermark_alpha)

    # Position the watermark closer to the bottom right corner
    watermark_width, watermark_height = watermark.size
    position = (image_width - watermark_width - 5, image_height - watermark_height - 5)

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