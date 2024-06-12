import os
import sys

from PIL import Image

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check is new/exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    clean_name = os.path.splitext(filename)[0]
    img.save(f"{output_folder}{clean_name}.png", "png")
    print("all done")

# buka cmd di file code ini berada lalu apa yang mau di rubah lalu bikin file baru
# python convert_to_png.py pokedex/ fileconvert/

# loop trough pokedex
# convert images to png format
# save to the new folder
