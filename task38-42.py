from random import choice, shuffle,random
from string import ascii_letters, digits


def generate_password(number_of_symbols):
    password = [choice(digits), choice(ascii_letters[0:26]), choice(ascii_letters[27:])]
    while len(password) < number_of_symbols:
        symbol = choice(ascii_letters + digits)
        if symbol not in password and symbol not in ['1', 'l', 'I', 'o', 'O', '0']:
            password.append(symbol)
    shuffle(password)
    return ''.join(password)


def main(number_of_passwords, number_of_symbols):
    passwords = [generate_password(number_of_symbols) for i in range(number_of_passwords)]
    return passwords
def monte_carlo(semi_pi):
    for i in range(1000000):
        if random() ** 2 + random() ** 2 <= 1:
            semi_pi += 1
    return (semi_pi / 1000000 * 4)

print('Случайны пароль из 7 символов', generate_password(7))
print('10 случайных паролей длиной 15 символов')
print(*main(10, 3), sep='\n')
print(*monte_carlo(0))
