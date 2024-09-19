from PIL import Image
import os
import argparse
#python lab2\\task5.py -d lab2\\Photos -ftype jpg


def create_thumbnail(input_image, size=(50, 50)):
    image = Image.open(input_image)
    image.thumbnail(size)
    return image


def main(input_dir, file_type):
    no_files = True
    for filename in os.listdir(input_dir):
        if filename.endswith("." + file_type):
            input_image = os.path.join(input_dir, filename)
            thumbnail = create_thumbnail(input_image)
            thumbnail.show()
            no_files = False
    if no_files:
        raise Exception("There are no files with this extension!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Thumbnail Viewer")
    parser.add_argument("-d", "--input_dir", type=str, help="Input directory path")
    parser.add_argument("-ftype", "--file_type", type=str, help="File extension to view")
    args = parser.parse_args()

    main(args.input_dir, args.file_type)
