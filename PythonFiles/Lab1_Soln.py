# Import PIL lib to manuplate the imgs
from PIL import Image
# Create an image with specified width and height
width = 512
height = 512
# using 3 channel RGB format
img = Image.new("RGB", (width, height), color="black")


# Save the img
img.save("PythonFiles/blackImage.png")
