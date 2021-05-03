def roots_of_quadratic_equation(a, b, c):
    if a != 0:
        d = b ** 2 - 4 * a * c
        if d == 0:
            return [-b / (2 * a)]
        elif d < 0:
            return ['NO']
        else:
            return [(-b - d ** 0.5) / (2 * a), (-b + d ** 0.5) / (2 * a)]
    else:
        if b != 0:
            return [-c / b]
        elif c == 0:
            return ['ALL']
        else:
            return ['NO']


result = roots_of_quadratic_equation(0, 2, 1)
print(*sorted(result))