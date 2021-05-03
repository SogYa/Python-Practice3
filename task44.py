from PIL import Image, ImageDraw


def board(num, size):
    side = num * size
    new_image = Image.new('RGB', (side, side), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    flag_black = True
    for i in range(0, side, size):
        if flag_black:
            for j in range(size, side, size * 2):
                draw.rectangle((j, i, j + size, i + size), fill=(255, 255, 255), width=size)
        else:
            for j in range(0, side, size * 2):
                draw.rectangle((j, i, j + size, i + size), fill=(255, 255, 255), width=size)
        flag_black = not flag_black
    new_image.save('board.png', 'png')


board(8, 50)
