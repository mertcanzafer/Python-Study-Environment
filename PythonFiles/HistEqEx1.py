from PIL import Image
import matplotlib.pyplot as plt

original = Image.open("PythonFiles/tiger.jpg")
original.show()
original = original.convert('L')

PixelVals = list(original.getdata())

width, height = original.size

totalPixels = width * height

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(PixelVals, bins=256, color='black', alpha=0.7)
plt.title('Histogram of Original Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Perform histogram equalization
equalized_pixels = list(original.histogram())

# Calculate and plot histogram for the equalized image
plt.subplot(1, 2, 2)
plt.hist(equalized_pixels, bins=256, color='black', alpha=0.7)
plt.title('Histogram of Equalized Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Show the histograms
plt.tight_layout()
plt.show()

h = list(original.histogram())

aMin = 0
aMax = 255
alow = 0
ahigh = 0
slow = 0.05
shigh = 1 - slow

for i in h:
    if (i >= totalPixels * slow):
        alow = min(i)
    else:
        ahigh = max(i)

for a in h:
    if (a > alow and a < ahigh):
        a = (((a - alow) / (ahigh - alow)) * (aMax - aMin)) + aMin
    elif (alow >= a):
        a = aMin
    elif (a >= ahigh):
        a = aMax

# aMin = 0
# aMax = 255
# alow = 0
# ahigh = 0
# slow = 0.05
# shigh = 1 - slow

# for i in equalized_pixels:
#     if (i >= totalPixels * slow):
#         alow = min(i)
#     else:
#         ahigh = max(i)

# for a in equalized_pixels:
#     if (a > alow and a < ahigh):
#         a = (((a - alow) / (ahigh - alow)) * (aMax - aMin)) + aMin
#     elif (alow >= a):
#         a = aMin
#     elif (a >= ahigh):
#         a = aMax

# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# plt.hist(PixelVals, bins=256, color='black', alpha=0.7)
# plt.title('Histogram of Original Image')
# plt.xlabel('Pixel Value')
# plt.ylabel('Frequency')

# plt.subplot(1, 2, 2)
# plt.hist(equalized_pixels, bins=256, color='black', alpha=0.7)
# plt.title('Histogram of Equalized Image')
# plt.xlabel('Pixel Value')
# plt.ylabel('Frequency')

# # Show the histograms
# plt.tight_layout()
# plt.show()
