from PIL import Image, ImageDraw

# Open the image
img = Image.open("PythonFiles/MyImg.png")
# black bacgroung color intensity
c0 = 0


class TopLeft:
    def __init__(self, x0, y0):
        self.x0 = x0
        self.y0 = y0


TopLeftList = []
y1L = []
x1L = []
cI = 0
counter = 0
width, height = img.size
visited = {i: 0 for i in range(256)}

for y in range(height):
    for x in range(width):
        if ((x > 0 and y > 0) and (x < 511 and y < 511)):

            if (img.getpixel((x, y)) != c0):

                if (img.getpixel((x, y-1)) == c0 and img.getpixel((x-1, y)) == c0):
                    TopLeftList.append(TopLeft(x, y))
                    cI = img.getpixel((x, y))
                    visited[cI] = 1
                elif (visited[img.getpixel((x, y))] != 1):
                    TopLeftList.append(TopLeft(x, y))
                    cI = img.getpixel((x, y))
                    visited[cI] = 1

                if (cI != img.getpixel((x, y))):
                    cI = img.getpixel((x, y))
                    # visited[cI] = 1
                    if (cI != img.getpixel((x-1, y)) and img.getpixel((x-1, y)) != c0 and visited[cI] != 1):
                        TopLeftList.append(TopLeft(x, y))
                    if (cI != img.getpixel((x, y + 1))):
                        y1L.append(y)
                        counter += 1
                    if (cI != img.getpixel((x + 1, y))):
                        x1L.append(x)
                    visited[cI] = 1
                if (cI != img.getpixel((x + 1, y)) and cI != img.getpixel((x, y-1))):
                    x1L.append(x)
                if (counter == 3 and cI != img.getpixel((x, y + 1)) and cI != img.getpixel((x-1, y))):
                    y1L.append(y)
                    counter += 1

            elif (img.getpixel((x + 1, y)) == c0 and img.getpixel((x, y-1)) == c0 and img.getpixel((x, y)) != c0):
                x1L.append(x)


for i in TopLeftList:
    print(i.x0)
    print(i.y0)
    print("------")
print(x1L)
print(y1L)
if img.mode != 'RGB':
    img = img.convert('RGB')

draw = ImageDraw.Draw(img)
draw.rectangle((TopLeftList[2].x0, TopLeftList[2].y0,
               x1L[2], y1L[1]), outline='blue', width=2)

draw.rectangle((TopLeftList[0].x0, TopLeftList[0].y0,
               x1L[0], y1L[4]), outline='blue', width=2)

draw.rectangle((TopLeftList[1].x0, TopLeftList[1].y0,
               x1L[1], y1L[2]), outline='blue', width=2)

draw.rectangle((TopLeftList[3].x0, TopLeftList[3].y0,
               x1L[3], 408), outline='blue', width=2)
draw.rectangle((TopLeftList[4].x0, TopLeftList[4].y0,
               x1L[4], 480), outline='blue', width=2)
# Save the modified image with blue boxes indicating the detected coordinates
img.save("PythonFiles/HW2Image.png")
