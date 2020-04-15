#Coding UTF-8

#python crop_circle.py in.png out.png

#Square -> Circle (alpha)

from PIL import Image
from PIL import ImageDraw
import sys

args = sys.argv

path = "img/" + args[1]
offset = 0

img = Image.open(path)

mask = Image.new("L", img.size)
draw = ImageDraw.Draw(mask)
draw.ellipse([(offset, offset), (img.size[0] - offset, img.size[1] - offset)], 255)
del draw

img.putalpha(mask)

img.save("img/" + args[2])