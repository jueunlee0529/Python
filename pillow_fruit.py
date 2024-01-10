from PIL import Image

fruit_img = Image.open("fruit.png")
fruit_rotated = fruit_img.rotate(270)
fruit_converted = fruit_img.convert('L')

print("fruit_converted.mode =", fruit_converted.mode)
print("fruit_img.size =", fruit_img.size)

fruit_converted.show()
fruit_rotated.show()
fruit_rotated.save("fruit_rotated.jpg")

