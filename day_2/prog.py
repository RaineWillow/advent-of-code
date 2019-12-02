import sys

lines = []

for line in sys.stdin:
 	lines.append(line.rstrip())

vals = lines[0].split(",")
for i in range(0, len(vals)):
	vals[i] = int(vals[i])

def prog1(valls):
	for x in range(0, len(valls), 4):
		if valls[x] == 99:
			break
		elif valls[x] == 1:
			op1 = valls[valls[x+1]]
			op2 = valls[valls[x+2]]
			valls[valls[x+3]] = op1 + op2
		elif valls[x] == 2:
			op1 = valls[valls[x+1]]
			op2 = valls[valls[x+2]]
			valls[valls[x+3]] = op1 * op2
	return valls[0]

def prog2(valls):
	for x in range(0, 100):
		for y in range(0, 100):
			newvals = valls[:]
			newvals[1] = x
			newvals[2] = y
			try:
				if prog1(newvals) == 19690720:
					print("result 2: " + str(x) + "|" + str(y))
			except:
				pass

print("result 1: " + str(prog1(vals[:])))
prog2(vals[:])
