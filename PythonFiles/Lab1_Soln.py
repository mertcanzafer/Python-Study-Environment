# Import PIL lib to manuplate the imgs
from PIL import Image, ImageDraw, ImageFont

# The ImageDraw module provides simple 2D graphics for Image objects. You can use this module to create new images, annotate or retouch existing images, and to generate graphics on the fly for web use.
# website :https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html

# Create an image with specified width and height
width = 512
height = 512
# using 1 channel L format
img = Image.new("L", (width, height), color="black")

# Save the img
img.save("PythonFiles/blackImage.png")

# To draw the shape inside our black img
# First, open your your image using open(C:\localPath) attribute
img = Image.open("PythonFiles/blackImage.png")

Draw_Obj = ImageDraw.Draw(img)

x0 = 255
y0 = 410
x1 = 450
y1 = 490
ColorIntensity = 120
Cbounds = (x0, y0, x1, y1)
# rectangle() method takes height and width values
Draw_Obj.rectangle(Cbounds, ColorIntensity, width=3)


# save the modified obj
img.save("PythonFiles/modifiedImg.png")
