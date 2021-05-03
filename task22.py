def defractalize(fractal):
    i = 0
    while fractal in fractal:
        if fractal[i] == fractal:
            del fractal[i]
            i -= 1
        i += 1                


fractal = [2, 5]
fractal.append(fractal)
fractal.append(fractal)
fractal.append(3)
fractal.append(fractal)
fractal.append(9)
print(id(fractal))
defractalize(fractal)
print(fractal)
