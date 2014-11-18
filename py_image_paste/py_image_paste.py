__author__ = 'hsuchih-kao'

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

logo = Image.open("logo.jpg")
#top_image = Image.open("main_image.jpg")
top_image = Image.new("RGB", (512, 512), "white")
top_image.paste(logo, (100, 100), None)
#top_image.thumbnail((128,128), Image.ANTIALIAS)

draw = ImageDraw.Draw(top_image)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 36)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((0, 0),"Sample Text", (0, 0, 0), font=font)

top_image.save("result.jpg")
top_image.show()