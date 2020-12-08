import sys
import pprint

lines = []

for line in sys.stdin:
 	lines.append(line.rstrip())

ruleset = dict()
for line in lines:
	line = line[:-1]
	line = line.split(" contain ")
	line[0] = line[0].rstrip("s").rstrip(" bag")
	line[1] = line[1].split(", ")
	line[1] = list(map(lambda x: x.rstrip("s").rstrip(" bag"), line[1]))
	ruleset[line[0]] = {}
	for bag in line[1]:
		if bag != "no other":
			num = int(bag[:2].rstrip())
			bag = bag[2:]
			ruleset[line[0]][bag] = num

pp = pprint.PrettyPrinter(indent=4)

def find(bag, rule):
	if bag in rule:
		return True
	else:
		for item in rule:
			if find(bag, ruleset[item]):
				return True

def count(bag):
	total_sum = 0
	if ruleset[bag] == {}:
		return total_sum
	else:
		for item in ruleset[bag]:
			total_sum += ruleset[bag][item] + ruleset[bag][item]*count(item)
		return total_sum

def prog1():
	sum = 0
	for rule in ruleset:
		sum += (1 if find("shiny gold", ruleset[rule]) else 0)

	return sum

def prog2():
	return count("shiny gold")

print("Result 1: " + str(prog1()))
print("Result 2: " + str(prog2()))
