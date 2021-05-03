def palindrome(s):
    s = ''.join(s.split()).upper()
    for i in range((int(len(s) / 2))):
        if s[i] != s[len(s) - 1 - i]:
            return 'Не палиндром'
    return 'Палиндром'


print(palindrome('А роза упала на лапу Азора'))
