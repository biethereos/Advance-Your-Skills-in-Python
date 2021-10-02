# Example file for Python Essential Libraries course by Joe Marini
# demonstrates image editing using the Pillow library
from PIL import Image, ImageDraw, ImageFont

infile = "ImagesArchive/Connections.jpeg"
# TODO: use the ImageDraw routines to modify an image
# with Image.open(infile) as img:
#     draw = ImageDraw.Draw(img)
#     draw.line((0, 0) + img.size, width=40, fill=128)
#     draw.line((0, img.size[1], img.size[0], 0), width=40, fill=128)
#     img.show()
# TODO: use the ImageDraw routines to modify an image
with Image.open(infile) as img:
    draw = ImageDraw.Draw(img)
    textstr = 'Hi, I\'m Hung'
    txtfont = ImageFont.truetype('arial.ttf', 75)
    txtsize = draw.textsize(textstr, font=txtfont)
    location = (20, img.height - txtsize[1])
    draw.text(location, textstr, (255, 255, 255), font=txtfont)
    img.show()
