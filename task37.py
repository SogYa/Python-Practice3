import sys


data = list(map(str.strip, sys.stdin))
for i in range(len(data)):
    if data[i][0] == '#':
        print(f'line {i + 1}: {data[i][1:].strip()}')


#import sys
#for line in sys.stdin:
	# rstrip(’\n’) 'отрезает' от строки line,
	# идущий справа символ перевода строки,
	# ведь print сам переводит строку
	#print(line.rstrip(’\n’))