from PIL import Image
import matplotlib.pyplot as plt

# Open the original image and convert it to grayscale
original = Image.open("PythonFiles/tiger.jpg")
original = original.convert('L')
original.show()
# Get the pixel values of the grayscale image
PixelVals = list(original.getdata())

# Get the dimensions (width and height) of the image
width, height = original.size

# Calculate the total number of pixels
totalPixels = width * height

# Calculate the histogram of the original image
h = original.histogram()

# Calculate the equalization limits
slow = 0.40
shigh = 1 - slow
aMin = 0
aMax = 255

# Calculate alow and ahigh
cumulative_sum = 0
alow = aMin
ahigh = aMax
for idx, freq in enumerate(h):
    cumulative_sum += freq
    if cumulative_sum >= totalPixels * slow:
        alow = idx
        break

cumulative_sum = 0
for idx, freq in enumerate(h[::-1]):
    cumulative_sum += freq
    if cumulative_sum >= totalPixels * slow:
        ahigh = 255 - idx
        break

# Apply manual histogram equalization
equalized_pixels = []
for pixel_value in PixelVals:
    if pixel_value < alow:
        equalized_pixels.append(aMin)
    elif pixel_value > ahigh:
        equalized_pixels.append(aMax)
    else:
        equalized_pixels.append(
            int(((pixel_value - alow) / (ahigh - alow)) * (aMax - aMin)) + aMin)

# Create a new image with equalized pixel values
equalized_image = Image.new('L', original.size)
equalized_image.putdata(equalized_pixels)

# Display original and equalized histograms
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(PixelVals, bins=256, color='black', alpha=0.7)
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
equalized_image.show()
