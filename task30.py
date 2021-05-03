def transformation(x): return x


values = [1, 23, 4222222, 'sdafasdf']
#transformation = lambda x: x                               # Не назначить лямбда выражениый, пользоваться def???
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')
