from PIL import Image, ImageFilter

# pip install pillow

img = Image.open("./astro.jpg")
# img = Image.open("./pokedex/pikachu.jpg")
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.convert("L")
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# crooked = filtered_img.rotate(90)
# resize = filtered_img.resize((300, 300))
# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))
# filtered_img.save("blur.png", "png")
# filtered_img.save("grey.png", "png")
# filtered_img.show()
# crooked.save("crooked.png", "png")
# resize.save("resized.png", "png")
# region.save("region.png", "png")

img.thumbnail((400, 400))
img.save("thumbnail.jpg")
