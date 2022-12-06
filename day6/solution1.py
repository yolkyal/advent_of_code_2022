line = open(0).read().strip()

c1, c2, c3, c4 = line[0:4]

for i in range(4, len(line)):
	if c1 != c2 and c1 != c3 and c1 != c4 and c2 != c3 and c2 != c4 and c3 != c4:
		print(i)
		break
	else:
		c1 = c2
		c2 = c3
		c3 = c4
		c4 = line[i]