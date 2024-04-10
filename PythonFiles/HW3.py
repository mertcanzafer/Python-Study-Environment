from PIL import Image
import matplotlib.pyplot as plt

# Open the original image

original = Image.open("PythonFiles/tiger.jpg")
original = original.convert('L')

original.show()

# Get the pixel values
pixelVals = list(original.getdata())

width, height = original.size

# Calculate the total pixels
totalPixels = width * height

# Calculate the original histogram
h = original.histogram()

# Calculate the equalization limits
slow = 0.10
shigh = 1 - slow

aMin = 0
aMax = 255

# Calculate alow and ahigh
cumulative_sum = 0
alow = aMin
ahigh = aMax
for i, num in enumerate(h):
    cumulative_sum += num
    if cumulative_sum >= totalPixels * slow:
        alow = i
        break

cumulative_sum = 0
for i, num in enumerate(h[::-1]):
    cumulative_sum += num
    if cumulative_sum >= totalPixels * slow:
        ahigh = 255 - i
        break

# Apply rules discussed in lecture slides
equalized_pixels = []
for pixel_value in pixelVals:
    if pixel_value < alow:
        equalized_pixels.append(aMin)
    elif pixel_value > ahigh:
        equalized_pixels.append(aMax)
    else:
        equalized_pixels.append(
            int(((pixel_value - alow) / (ahigh - alow)) * (aMax - aMin)) + aMin)

# Create a new img
result_image = Image.new('L', original.size)
result_image.putdata(equalized_pixels)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(pixelVals, bins=256, color='black', alpha=0.7)
plt.title('Histogram of Original Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(equalized_pixels, bins=256, color='black', alpha=0.7)
plt.title('Histogram of Equalized Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Show the equalized image
result_image.show()
