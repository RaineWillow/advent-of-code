import sys

lines = []

for line in sys.stdin:
 	lines.append(int(line.rstrip()))

def prog1():
	for i in range(25, len(lines)):
		found = False
		for j in range(i-25, i):
			for k in range(j+1, i):
				if lines[i] == lines[j] + lines[k]:
					found = True
					break
			if found == True:
				break

		if found == False:
			return lines[i]

def prog2():
	num = 144381670
	past_nums = []
	for i in range(0, len(lines)):
		past_nums = []
		if i == 562:
			continue
		total = lines[i]
		past_nums.append(lines[i])
		for j in range(i+1, len(lines)):
			if i == 562:
				continue
			total += lines[j]
			past_nums.append(lines[j])
			if total > num:
				break
			if total == num:
				past_nums.sort()
				return past_nums[0] + past_nums[len(past_nums)-1]


print("Result 1: " + str(prog1()))
print("Result 2: " + str(prog2()))
