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

def prog1():
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
	pass

print("Result 1: " + str(prog1()))
print("Result 2: " + str(prog2()))
