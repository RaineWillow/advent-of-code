import sys

lines = []

for line in sys.stdin:
 	lines.append(line.rstrip())

instruct1 = lines[0].split(",")
instruct2 = lines[1].split(",")

def prog1(instruct1, instruct2):
	wire1Points = set()
	intersectList = []
	key = {'R' : "+", 'L' : "-", 'U' : "+", 'D' : "-"}

	w1x = 0
	w1y = 0
	for w1 in instruct1:
		if w1[0] == 'R' or w1[0] == 'L':
			for x in range(w1x, w1x + int(key[w1[0]] + w1[1:])+int(key[w1[0]] + "1"), int(key[w1[0]] + "1")):
				w1x = x
				wire1Points.add((w1x, w1y))
		else:
			for y in range(w1y, w1y + int(key[w1[0]] + w1[1:])+int(key[w1[0]] + "1"), int(key[w1[0]] + "1")):
				w1y = y
				wire1Points.add((w1x, w1y))

	w2x = 0
	w2y = 0
	for w2 in instruct2:
		if w2[0] == 'R' or w2[0] == 'L':
			for x in range(w2x, w2x + int(key[w2[0]] + w2[1:])+int(key[w2[0]] + "1"), int(key[w2[0]] + "1")):
				w2x = x
				if (w2x, w2y) in wire1Points:
					intersectList.append((w2x, w2y))
		else:
			for y in range(w2y, w2y + int(key[w2[0]] + w2[1:])+int(key[w2[0]] + "1"), int(key[w2[0]] + "1")):
				w2y = y
				if (w2x, w2y) in wire1Points:
					intersectList.append((w2x, w2y))

	smallDis = None
	for inter in intersectList:
		if inter == (0, 0):
			pass
		else:
			interx, intery = inter
			dist = abs(interx) + abs(intery)
			if smallDis == None:
				smallDis = dist
			else:
				if smallDis > dist:
					smallDis = dist
	return smallDis

def prog2(instruct1, instruct2):
	wire1Points = {}
	intersectList = []
	key = {'R' : "+", 'L' : "-", 'U' : "+", 'D' : "-"}

	w1x = 0
	w1y = 0
	step1 = 0
	for w1 in instruct1:
		if w1[0] == 'R' or w1[0] == 'L':
			for x in range(w1x, w1x + int(key[w1[0]] + w1[1:])+int(key[w1[0]] + "1"), int(key[w1[0]] + "1")):
				w1x = x
				if (w1x, w1y) not in wire1Points:
					step1 += 1
					wire1Points[(w1x, w1y)] = step1
		else:
			for y in range(w1y, w1y + int(key[w1[0]] + w1[1:])+int(key[w1[0]] + "1"), int(key[w1[0]] + "1")):
				w1y = y
				if (w1x, w1y) not in wire1Points:
					step1 += 1
					wire1Points[(w1x, w1y)] = step1

	w2x = 0
	w2y = 0
	step2 = 0
	wire2Points = {}
	for w2 in instruct2:
		if w2[0] == 'R' or w2[0] == 'L':
			for x in range(w2x, w2x + int(key[w2[0]] + w2[1:])+int(key[w2[0]] + "1"), int(key[w2[0]] + "1")):
				w2x = x
				if (w2x, w2y) in wire1Points:
					intersectList.append((w2x, w2y))
				if (w2x, w2y) not in wire2Points:
					step2 += 1
					wire2Points[(w2x, w2y)] = step2
		else:
			for y in range(w2y, w2y + int(key[w2[0]] + w2[1:])+int(key[w2[0]] + "1"), int(key[w2[0]] + "1")):
				w2y = y
				if (w2x, w2y) in wire1Points:
					intersectList.append((w2x, w2y))
				if (w2x, w2y) not in wire2Points:
					step2 += 1
					wire2Points[(w2x, w2y)] = step2

	smallDis = None
	for inter in intersectList:
		if inter == (0, 0):
			pass
		else:
			dist = wire1Points[inter] + wire2Points[inter]
			if smallDis == None:
				smallDis = dist
			else:
				if smallDis > dist:
					smallDis = dist
	return smallDis

print("Result 1: " + str(prog1(instruct1[:], instruct2[:])))
print("Result 2: " + str(prog2(instruct1[:], instruct2[:])))
