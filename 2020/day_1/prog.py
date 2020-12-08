import sys

lines = []

for line in sys.stdin:
 	lines.append(line.rstrip())

def prog1():
	data = {int(l) for l in lines}
	for x in data:
		test = 2020-x
		if test in data:
			return test*x

def prog2():
	data = {int(l) for l in lines}
	for x in data:
		test = 2020-x
		data2 = data.copy()
		data2.remove(x)
		for y in data2:
			test2 = test-y
			if test2 in data:
				return x*y*test2


print("Result 1: " + str(prog1()))
print("Result 2: " + str(prog2()))
