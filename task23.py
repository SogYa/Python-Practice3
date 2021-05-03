def fractal_print(obj):
  print('[' + ', '.join(map(str, obj)) + ']')
fractal = [3]
fractal.append(fractal)
fractal_print(fractal)