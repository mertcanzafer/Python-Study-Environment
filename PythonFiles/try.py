PixelVals = [1, 1, 0, 0, 2, 2, 2, 2, 5, 5]

dict = {}

for i in range(0, 6):
    dict[i] = 0


for i in dict.keys():
    for j in PixelVals:
        if (i == j):
            dict[i] += 1

print(dict)
