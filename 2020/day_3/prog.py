import sys

lines = []

for line in sys.stdin:
 	lines.append(line.rstrip())

def prog1(right, down):
	num_trees = 0
	loc_x = 0
	loc_y = 0
	tile_width = len(lines[0])
	tile_length = len(lines)
	while True:
		if (loc_y >= tile_length):
			break

		if (lines[loc_y][loc_x % tile_width] == "#"):
			num_trees += 1

		loc_x += right
		loc_y += down

	return num_trees


def prog2():
	return prog1(1, 1) * prog1(3, 1) * prog1(5, 1) * prog1(7, 1) * prog1(1, 2)

print("Result 1: " + str(prog1(3, 1)))
print("Result 2: " + str(prog2()))
