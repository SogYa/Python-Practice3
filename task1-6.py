def print_shrug_smile():   # 18.1
    print('¯\\_(ツ)_/¯')

def print_ktulhu_smile():
    print('{:€')

def print_happy_smile():
    print('(͡°ʖ ͡°)')

def asc_password():   # 18.2
    flag = False
    for i in range(3):
        if not flag and input() == 'password':
            return print('Пароль принят')
    print('В доступе отказано')

def golden_ratio(i):
    a, b = 0, 1
    n = 1
    while n <= i:
        a, b = b, a + b
        n += 1
        if n == i - 1:
            b1 = b
    return(b1 / b)

def bracket_check(test_string):   # 18.4
    result = 0
    for a in test_string:
        if "(" in a:
            result += 1
        elif ")" in a:
            result -= 1
        if result < 0:
            return print('NO')
    if result > 0:
        return print('NO')
    return print('YES')

def equation(xy1, xy2):
    x1 = int(xy1.split(";")[0])
    y1 = int(xy1.split(";")[1])
    x2 = int(xy2.split(";")[0])
    y2 = int(xy2.split(";")[1])
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(k, b)

def line(s, t):   # 18.6
    k, b = [float(elem) for elem in s.split('x')]
    x, y = [float(elem) for elem in t.split(';')]
    print(y == k * x + b)


func = input()
while func != '':
    exec(func)
    func = input()