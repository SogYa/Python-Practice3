import sys


print(any(map(lambda x: int(x) == 0, [x for elem in list(sys.stdin) for x in elem.split(' ')])))
