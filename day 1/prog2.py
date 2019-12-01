import sys
from math import floor
lines = []

def getFuel(fuel):
	if (fuel <= 0):
		return 0
	else:
		return fuel+getFuel(floor(fuel/3) - 2)

for line in sys.stdin:
 	lines.append(int(line.rstrip()))

sum = 0

for x in lines:
	fuel = floor(x/3) - 2
	sum += (getFuel(fuel))

print(sum)
