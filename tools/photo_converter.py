"""Class and CLI tools to convert images."""
import argparse
import os
import pathlib

from PIL import Image, UnidentifiedImageError


class PhotoConverter:
    @staticmethod
    def convert(src: str, dst: str) -> None:
        fname, _ = src.split(os.sep)[-1].split(".")
        img = Image.open(src)
        dst_ext = dst.split(".")[-1]
        pathlib.Path(dst).parent.mkdir(parents=True, exist_ok=True)
        img.save(dst, dst_ext)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Image Converter",
        description="Convert Images",
    )
    parser.add_argument("--output-extension")
    parser.add_argument("-d", "--directory")
    args = parser.parse_args()

    for relpath in os.listdir(args.directory):
        path = args.directory + relpath
        try:
            image = Image.open(path)
        except UnidentifiedImageError:
            continue
        filename, _ = relpath.split(".")
        new_path = "".join([args.directory, filename, ".", args.output_extension])
        PhotoConverter.convert(path, new_path)