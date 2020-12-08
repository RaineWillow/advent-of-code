import sys
import pprint

lines = []

for line in sys.stdin:
 	lines.append(line.rstrip())

passports = []
current_passport = dict()
for i, line in enumerate(lines):
	if (line == ''):
		passports.append(current_passport)
		current_passport = dict()
	else:
		line = line.split(" ")
		for entry in line:
			current_passport[entry.split(":")[0]] = entry.split(":")[1]

	if (i+1 == len(lines)):
		passports.append(current_passport)
		current_passport = dict()

pp = pprint.PrettyPrinter(indent=4)

def prog1():
	checks = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	count = 0
	for passport in passports:
		output = True
		for check in checks:
			if check not in passport:
				output = False
				break
		if (output):
			count += 1

	return count

def prog2():
	checks = [{'byr': {'r': [1920, 2002]}}, {'iyr': {'r': [2010, 2020]}}, {'eyr': {'r': [2020, 2030]}}, {'hgt': {'h': {'cm': [150, 193], 'in': [59, 76]}}}, {'hcl': {'c': ''}}, {'ecl': {'e': {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}}}, {'pid': {'l': ''}}]
	#pp.pprint(checks)
	count = 0
	for passport in passports:
		output = True
		for check in checks:
			curr_type = list(check.keys())[0]
			if curr_type not in passport:
				output = False
				break
			else:
				try:
					valid_type = list(check[curr_type].keys())[0]
					if (valid_type == 'r'):
						if not (int(passport[curr_type]) >= check[curr_type][valid_type][0] and int(passport[curr_type]) <= check[curr_type][valid_type][1]):
							output = False
							break
					elif (valid_type == 'h'):
						if (passport[curr_type][-2:] == 'cm'):
							value = int(passport[curr_type][:3])
							if not (value >= check[curr_type][valid_type]['cm'][0] and value <= check[curr_type][valid_type]['cm'][1]):
								output = False
								break
						elif (passport[curr_type][-2:] == 'in'):
							value = int(passport[curr_type][:2])
							if not (value >= check[curr_type][valid_type]['in'][0] and value <= check[curr_type][valid_type]['in'][1]):
								output = False
								break
						else:
							output = False
							break
					elif (valid_type == 'c'):
						if (len(passport[curr_type]) == 7):
							test = int(passport[curr_type].replace("#", "0x"), 16)
						else:
							output = False
							break
					elif (valid_type == 'e'):
						if not passport[curr_type] in check[curr_type][valid_type]:
							output = False
							break
					elif (valid_type == 'l'):
						if not (len(passport[curr_type]) == 9):
							output = False
							break
						else:
							test = int(passport[curr_type])
				except:
					output = False
					break
		if (output):
			print(passport['hgt'])
			count += 1

	return count

print("Result 1: " + str(prog1()))
print("Result 2: " + str(prog2()))
