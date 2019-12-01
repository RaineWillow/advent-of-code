import sys
from math import floor
lines = []

for line in sys.stdin:
 	lines.append(int(line.rstrip()))

sum = 0

for x in lines:
	sum += floor(x/3) - 2

print(sum)
