import sys

lines = []

for line in sys.stdin:
 	lines.append(line.rstrip())

def prog1():
	current_data = [False] * 26
	sum = 0
	for line in lines:
		if line == "":
			for found in current_data:
				sum += (1 if found else 0)
			current_data = [False] * 26
		else:
			for i in range(0, len(line)):
				current_data[ord(line[i]) - 97] = True

	for found in current_data:
		sum += (1 if found else 0)

	return sum

def prog2():
	current_data = [True] * 26
	sum = 0
	for line in lines:
		if line == "":
			for found in current_data:
				sum += (1 if found else 0)
			current_data = [True] * 26
		else:
			constructed_list = [False] * 26
			for i in range(0, len(line)):
				constructed_list[ord(line[i]) - 97] = True
			current_data = map(lambda x, y: x and y, current_data, constructed_list)

	for found in current_data:
		sum += (1 if found else 0)

	return sum

print("Result 1: " + str(prog1()))
print("Result 2: " + str(prog2()))
