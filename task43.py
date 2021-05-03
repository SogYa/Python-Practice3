from PIL import Image, ImageDraw


def gradient(color):
    new_image = Image.new('RGB', (512, 200), (0, 0, 0))
    pixels = new_image.load()
    saturation = 0
    for i in range(0, 512, 2):
        for j in range(200):
            if color == 'R':
                pixels[i, j], pixels[i + 1, j] = (saturation, 0, 0), (saturation, 0, 0)
            elif color == 'G':
                pixels[i, j], pixels[i + 1, j] = (0, saturation, 0), (0, saturation, 0)
            elif color == 'B':
                pixels[i, j], pixels[i + 1, j] = (0, 0, saturation), (0, 0, saturation)
        saturation += 1
    new_image.save('gradient.png', 'PNG')


def gradient_with_line(color):
    new_image = Image.new('RGB', (512, 200), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    saturation = 0
    for i in range(0, 512, 2):
        if color == 'R':
            draw.line((i, 0, i, 200), fill=(saturation, 0, 0), width=2)
        elif color == 'G':
            draw.line((i, 0, i, 200), fill=(0, saturation, 0), width=2)
        elif color == 'B':
            draw.line((i, 0, i, 200), fill=(0, 0, saturation), width=2)
        saturation += 1
    new_image.save('gradient.png', 'PNG')


gradient_with_line('B')
