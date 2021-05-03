from PIL import Image


def make_preview(size, n_colors):
    im_c = Image.open('izm.jpg')
    im_c.thumbnail(size)
    im_c = im_c.convert('P', palette=Image.WEB, colors=n_colors)
    im_c.save('res.bmp', 'BMP')


make_preview((400, 200), 64)
