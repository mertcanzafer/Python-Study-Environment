from PIL import Image

original = Image.open("PythonFiles/tiger.jpg")

original.show()
original = original.convert('L')

PixelVals = list(original.getdata())

maxVal = max(PixelVals)
minVal = min(PixelVals)
pixel_counts = [0] * (maxVal + 1)
for val in PixelVals:
    pixel_counts[val] += 1

# Calculate cumulative distribution function (CDF)
cdf = [0] * (maxVal + 1)
sum = 0
for i in range(maxVal + 1):
    sum += pixel_counts[i]
    cdf[i] = sum

total_pixels = len(PixelVals)
normalized_cdf = [cdf_val / total_pixels for cdf_val in cdf]


equalized_pixels = [round(normalized_cdf[val] * maxVal)
                    for val in PixelVals]

equalized_image = Image.new('L', original.size)
equalized_image.putdata(equalized_pixels)

equalized_image.show()
