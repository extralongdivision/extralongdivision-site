"""Converts all files in working directory to png."""
import os
from PIL import Image

for relpath in os.listdir():
    if relpath.endswith(".webp"):
        filename, _ = relpath.split(".")
        image = Image.open(relpath)
        image.save(filename + ".png", "png")