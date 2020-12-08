import sys

lines = []

for line in sys.stdin:
 	lines.append(line.rstrip())

print("Num lines: " + str(len(lines)))

def prog1():
	valid_count = 0
	for password in lines:
		password = password.replace(":", "").split(" ")
		password[0] = password[0].split("-")
		letter_count = password[2].count(password[1])
		if (letter_count >= int(password[0][0]) and letter_count <= int(password[0][1])):
			valid_count += 1
	return valid_count


def prog2():
	valid_count = 0
	for password in lines:
		password = password.replace(":", "").split(" ")
		password[0] = password[0].split("-")
		password[0][0] = str(int(password[0][0]) - 1)
		password[0][1] = str(int(password[0][1]) - 1)
		if ((password[2][int(password[0][0])] == password[1]) ^ (password[2][int(password[0][1])] == password[1])):
			valid_count += 1
	return valid_count

print("Result 1: " + str(prog1()))
print("Result 2: " + str(prog2()))
