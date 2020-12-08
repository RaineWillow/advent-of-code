import sys
import math

lines = []

for line in sys.stdin:
 	lines.append(line.rstrip())

def list_duplicates(seq):
  seen = set()
  seen_add = seen.add
  seen_twice = set(x for x in seq if x in seen or seen_add(x))
  return list(seen_twice )

def prog1(rhs, lhs):
	numList = 0
	for x in range(rhs, lhs+1):
		digits = [(x//(10**i))%10 for i in range(math.ceil(math.log(x, 10))-1, -1, -1)]

		truth = True
		lastDig = 0
		for i in digits:
			if lastDig == 0:
				lastDig = i
			else:
				if lastDig <= i:
					truth = True
					lastDig = i
				else:
					truth = False
					break

		if list_duplicates(digits) != []:
			if truth == True:
				numList += 1

	return numList



def prog2(rhs, lhs):
	numList = 0
	for x in range(rhs, lhs+1):
		digits = [(x//(10**i))%10 for i in range(math.ceil(math.log(x, 10))-1, -1, -1)]

		truth = True
		lastDig = 0
		for i in digits:
			if lastDig == 0:
				lastDig = i
			else:
				if lastDig <= i:
					truth = True
					lastDig = i
				else:
					truth = False
					break

		dupList = list_duplicates(digits)
		if dupList != []:
			if truth == True:
				dup1 = False
				for dups in dupList:
					if digits.count(dups) < 3:
						dup1 = True
						break
				if dup1:
					numList += 1

	return numList

print("Result 1: " + str(prog1(int(lines[0].split("-")[0]), int(lines[0].split("-")[1]))))
print("Result 2: " + str(prog2(int(lines[0].split("-")[0]), int(lines[0].split("-")[1]))))
