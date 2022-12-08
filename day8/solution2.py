data = []
with open(0) as f:
	for line in f:
		row = list(line.strip())
		data.append(list(map(int, row)))

num_rows = len(data)
num_cols = len(data[0])

best_score = -1
for r in range(1, num_rows - 1):
	for c in range(1, num_cols - 1):
		score = [0, 0, 0, 0]
		checked = data[r][c]
		# LEFT
		for tree in reversed([data[r][c2] for c2 in range(c)]):
			if tree < checked:
				score[0] += 1
			elif tree >=  checked:
				score[0] += 1
				break
		
		# RIGHT
		for tree in [data[r][c2] for c2 in range(c+1, num_cols)]:
			if tree < checked:
				score[1] += 1
			elif tree >=  checked:
				score[1] += 1
				break
		
		# UP
		for tree in reversed([data[r2][c] for r2 in range(r)]):
			if tree < checked:
				score[2] += 1
			elif tree >=  checked:
				score[2] += 1
				break
		
		# DOWN
		for tree in [data[r2][c] for r2 in range(r+1, num_rows)]:
			if tree < checked:
				score[3] += 1
			elif tree >=  checked:
				score[3] += 1
				break
		
		score = score[0] * score[1] * score[2] * score[3]
		best_score = max(score, best_score)

print(best_score)