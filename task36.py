import sys


def value(word):
    result = 0
    for i in range(len(word)):
        result += ord(word[i].upper()) - ord('A') + 1
    return result


print('\n'.join(sorted(sorted(list(map(str.strip, sys.stdin))), key=value)))
