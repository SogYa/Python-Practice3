def solve(*coefficients):
    if len(coefficients) == 3:
        d = coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2]
        if d == 0:
            return [-coefficients[1] / (2 * coefficients[0])]
        elif d < 0:
            return ['NO']
        else:
            return ([(-coefficients[1] - d ** 0.5) / (2 * coefficients[0]), (-coefficients[1] + d ** 0.5) /
                    (2 * coefficients[0])])
    elif len(coefficients) == 2:
        if coefficients[0] != 0:
            return [-coefficients[1] / coefficients[0]]
        elif coefficients[1] == 0:
            return ['ALL']
        else:
            return ['NO']
    elif len(coefficients) == 1:
        if coefficients[0] == 0:
            return ['ALL']
        else:
            return ['NO']
    else:
        return ['NO']


print(*sorted(solve(*list(map(int, input().split(' '))))))