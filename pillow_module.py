from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

lion_img = Image.open("lion.jpg")
c3coding_img = Image.open("c3coding.jpg")
c3coding_img.thumbnail((120, 120))
draw = ImageDraw.Draw(lion_img)

stx, sty = (150, 285)
c3x, c3y = c3coding_img.size
msg1 = "The               is"
msg2 = "the Best!"

# mfont = ImageFont.truetype("FRADM.TTF", 40)
# m2font = ImageFont.truetype("BROADW.TTK", 52)
m3font = ImageFont.load_default()
         
draw.text((70, 280), msg1, (255, 255, 0), font = m3font, align = "Left")
draw.text((70, 330), msg2, (255, 0, 0), font = m3font, align = "Left")
lion_img.paste(c3coding_img, (stx, sty, stx + c3x, sty + c3y))

lion_img.show()
lion_img.save("c3lion.jpg")
