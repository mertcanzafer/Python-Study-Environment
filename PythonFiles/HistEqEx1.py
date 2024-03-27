from PIL import Image

original = Image.open("PythonFiles/tiger.jpg")

original.show()
original = original.convert('L')

PixelVals = list(original.getdata())

aHigh = max(PixelVals)
aLow = min(PixelVals)
pixel_counts = [0] * (aHigh + 1)
for val in PixelVals:
    pixel_counts[val] += 1

# Calculate cumulative distribution function (CDF)
cdf = [0] * (aHigh + 1)
sum = 0
for i in range(aHigh + 1):
    sum += pixel_counts[i]
    cdf[i] = sum

total_pixels = len(PixelVals)
normalized_cdf = [cdf_val / total_pixels for cdf_val in cdf]

sLow = 120
sHigh = 220  # Use the maximum pixel value for grayscale images

d = max(normalized_cdf)
c = min(normalized_cdf)

newCdf = [
    round(((cdf_val - c) /
          (d - c)) * (sHigh - sLow) + sLow)
    for cdf_val in normalized_cdf
]

equalized_pixels = [newCdf[val] for val in PixelVals]

equalized_image = Image.new('L', original.size)
equalized_image.putdata(equalized_pixels)

equalized_image.show()
