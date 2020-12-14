import sys

lines = []

for line in sys.stdin:
 	lines.append(line.rstrip())

accumulator = 0
mem_ptr = 0

def execute(instruction, value):
	global accumulator
	global mem_ptr
	if instruction == "nop":
		mem_ptr += 1
	elif instruction == "acc":
		accumulator += value
		mem_ptr += 1
	elif instruction == "jmp":
		mem_ptr += value

def reset():
	global accumulator
	global mem_ptr
	mem_ptr = 0
	accumulator = 0

def prog1():
	reset()
	execute_record = set()
	while True:
		if not mem_ptr in execute_record:
			execute_record.add(mem_ptr)
			instruction = lines[mem_ptr].split(" ")
			execute(instruction[0], int(instruction[1]))
		else:
			break
	return accumulator

def prog2():
	reset()
	for i in range(0, len(lines)):
		reset()
		data = lines.copy()
		if lines[i][:3] == "jmp":
			data[i] = "nop" + lines[i][3:]
		elif lines[i][:3] == "nop":
			data[i] = "jmp" + lines[i][3:]

		execute_record = set()
		failed = False
		while True:
			if not mem_ptr in execute_record:
				if (mem_ptr >= len(data)):
					break
				execute_record.add(mem_ptr)
				instruction = data[mem_ptr].split(" ")
				execute(instruction[0], int(instruction[1]))
			else:
				failed = True
				break
		if not failed:
			break
	return accumulator


print("Result 1: " + str(prog1()))
print("Result 2: " + str(prog2()))
