import sys
from math import floor
lines = []

for line in sys.stdin:
 	lines.append(int(line.rstrip()))

def getFuel(fuel):
	if (fuel <= 0):
		return 0
	else:
		return fuel+getFuel(floor(fuel/3) - 2)

def prog1():
	sum = 0
	for x in lines:
		sum += floor(x/3) - 2
	return sum

def prog2():
	sum = 0
	for x in lines:
		fuel = floor(x/3) - 2
		sum += (getFuel(fuel))
	return sum

print("Result 1: " + str(prog1()))
print("Result 2: " + str(prog2()))
