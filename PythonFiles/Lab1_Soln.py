# Import PIL lib to manuplate the imgs
from PIL import Image, ImageDraw, ImageFont
import random

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

# Ask user to input a number to draw that number of shapes inside the img
print("Enter a number: ")
n = int(input())
Draw_Obj = ImageDraw.Draw(img)


def draw():
    # Iterate over n times to draw shapes
    for i in range(0, n):
        # generate coordinates of rectangles randomly
        x0 = random.randint(0, 511)
        y0 = random.randint(0, 511)

        if (x0 == 511 or y0 == 511):
            raise ("Invalid bound error occured!!")

        x1 = random.randint(x0, 511)
        y1 = random.randint(y0, 511)

        # Condition 1
        if ((x1 - x0) * (y1 - y0) < 10 * 10 or (x1 - x0) * (y1 - y0) > 200 * 200):
            raise ("Conditions shoud satisfy the rules!!!")

        # draw the rectangle
        Cbounds = (x0, y0, x1, y1)
        #  Condition 2 generate Color intensity randomly
        ColorIntensity = random.randint(100, 255)
        Draw_Obj.rectangle(Cbounds, ColorIntensity, width=3)


draw()
# save the modified obj
img.save("PythonFiles/modifiedImg.png")
