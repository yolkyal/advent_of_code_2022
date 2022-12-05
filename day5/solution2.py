stacks = []
for i in range(10):
	stacks.append([])

with open(0) as f:
	while True:
		line = next(f)
		if line[1] == '1':
			break
		else:
			for i, c in enumerate(line):
				if c == '[':
					stacks[(i // 4) + 1].append(line[i+1])
	
	next(f)
	for line in f:
		m, f, t = list(map(int, line.strip().replace('move', '').replace('from', '').replace('to', '').split()))
		stacks[t] = stacks[f][:m] + stacks[t]
		stacks[f] = stacks[f][m:]
	
	result = ''.join([stack[0] for stack in stacks if len(stack) > 0])
	print(result)