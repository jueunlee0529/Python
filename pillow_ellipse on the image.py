from PIL import Image
from PIL import ImageDraw

lion_img = Image.open("lion.jpg")
circle_area = [(0, 160), (1280, 900)]

draw_imgs = ImageDraw.Draw(lion_img)
draw_imgs.ellipse(circle_area, outline = "yellow", width = 10)

lion_img.show()
lion_img.save("imagedraw.jpg")
