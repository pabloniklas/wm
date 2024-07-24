import sys
from lib_wm import process_images

def main():
    image_files = sys.argv[1:]
    if not image_files:
        print("Usage: wm <list of image files>")
        sys.exit(1)

    process_images(image_files)

if __name__ == "__main__":
    main()
