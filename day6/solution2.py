line = open(0).read().strip()

s = set(line[0:14])

for i in range(1, len(line) - 14):
	if len(s) == 14:
		print(i+13)
		break
	else:
		s = set(line[i: i+14])