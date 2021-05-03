def encrypt_caesar(msg, shift=3):
    cipher = ''
    for i in range(len(msg)):
        if ord('А') <= ord(msg[i]) <= ord('Я'):
            if ord('А') <= ord(msg[i]) + shift <= ord('Я'):
                cipher += chr(ord(msg[i]) + shift)
            elif ord('Я') <= ord(msg[i]) + shift:
                cipher += chr(ord('А') + (ord(msg[i]) + shift - 1 - ord('Я')))
            elif ord('А') >= ord(msg[i]) + shift:
                cipher += chr(ord('Я') + (ord(msg[i]) + shift + 1 - ord('А')))

        elif ord('а') <= ord(msg[i]) <= ord('я'):
            if ord('а') <= ord(msg[i]) + shift <= ord('я'):
                cipher += chr(ord(msg[i]) + shift)
            elif ord('я') <= ord(msg[i]) + shift:
                cipher += chr(ord('а') + (ord(msg[i]) + shift - ord('я') - 1))
            elif ord('а') >= ord(msg[i]) + shift:
                cipher += chr(ord('я') + (ord(msg[i]) + shift + 1 - ord('а')))
        else:
            cipher += msg[i]
    return cipher


def decrypt_caesar(msg, shift=3):
    return encrypt_caesar(msg, -shift)


text = 'АБВЭЮЯ 111 абвэюя!'
step = -1
encrypted = encrypt_caesar(text)
decrypted = decrypt_caesar(encrypted)
print(encrypted)
print(decrypted)