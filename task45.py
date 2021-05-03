from PIL import Image


def makeanagliph(filename, delta):
    im_1 = Image.open(filename)
    im_2 = im_1.copy()
    pixels = im_1.load()
    pixels_r = im_2.load()
    x, y = im_1.size
    for i in range(delta, x):
        for j in range(y):
            r, g, b, = pixels[i, j]
            pixels[i, j] = pixels_r[i - delta, j][0], g, b
    im_1.save('stereo.png', 'PNG')


makeanagliph('izm.jpg', 20)
