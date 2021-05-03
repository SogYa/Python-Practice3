from PIL import Image


def image_filter(pixs, i, j):
    """делает осень"""
    r, g, b = pixs[i, j]
    if r + b < g:
        r += 50
        b -= 100
        g -= 30
    return r, g, b


im = Image.open('izm.jpg')
im_cp = im.copy()
pixels = im.load()
pixels_cp = im_cp.load()
x, y = im.size
for i in range(x):
    for j in range(y):
        pixels[i, j] = image_filter(pixels_cp, i, j)
im.show()
