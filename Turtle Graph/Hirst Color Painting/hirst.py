import colorgram
rgbColors = []
colors = colorgram.extract('/Users/wheezy/Desktop/100DaysOfCoding (Python)/Turtle Graph/Hirst Color Painting/image.jpg', 25)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    newColor = (r, g, b)
    rgbColors.append(newColor)

print(rgbColors)
    
colorList = [(236, 35, 108), (222, 231, 237), (145, 28, 65), (239, 74, 34), (6, 148, 93), (231, 238, 234), (232, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (172, 36, 98), (246, 219, 44), (42, 172, 112), (216, 130, 165), (216, 58, 26), (235, 164, 190), (156, 25, 22), (20, 189, 230), (238, 169, 157), (162, 210, 182)]