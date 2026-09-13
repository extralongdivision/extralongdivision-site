"""Converts all files in working directory to webp."""
import os
from PIL import Image

for relpath in os.listdir():
    if relpath.endswith(".jpg") or relpath.endswith(".jpeg"):
        filename, _ = relpath.split(".")
        image = Image.open(relpath)
        image.save(filename + ".webp", "webp")