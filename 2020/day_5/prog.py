import sys

lines = []

for line in sys.stdin:
 	lines.append(line.rstrip())

def getRow(data):
	row = 0
	for i in range(0, 7):
		row += (2**i if data[6-i] == "B" else 0)
	return row

def getColumn(data):
	column = 0
	for i in range(0, 3):
		column += (2**i if data[9-i] == "R" else 0)
	return column

def prog1():
	highest_num = 0
	for item in lines:
		current_num = getRow(item) * 8 + getColumn(item)
		if (current_num > highest_num):
			highest_num = current_num

	return highest_num


def prog2():
	seatIDs = []
	for item in lines:
		seatIDs.append(getRow(item) * 8 + getColumn(item))
	seatIDs.sort()
	for i in range(0, len(seatIDs)):
		if not ((i-1 < 0) or (i+1 >= len(seatIDs))):
			if (seatIDs[i+1] > seatIDs[i]+1):
				return seatIDs[i]+1


print("Result 1: " + str(prog1()))
print("Result 2: " + str(prog2()))
