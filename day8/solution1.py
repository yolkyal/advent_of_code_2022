data = []
with open(0) as f:
	for line in f:
		row = list(line.strip())
		data.append(list(map(int, row)))

num_rows = len(data)
num_cols = len(data[0])

total = num_cols * 2 + (num_rows - 2) * 2
for r in range(1, num_rows - 1):
	for c in range(1, num_cols - 1):
		checked = data[r][c]
		# LEFT
		if all([data[r][c2] < checked for c2 in range(c)]):
			total += 1
			continue
		
		# RIGHT
		if all([data[r][c2] < checked for c2 in range(c+1, num_cols)]):
			total += 1
			continue
		
		# UP
		if all([data[r2][c] < checked for r2 in range(r)]):
			total += 1
			continue
		
		# DOWN
		if all([data[r2][c] < checked for r2 in range(r+1, num_rows)]):
			total += 1
			continue

print(total)