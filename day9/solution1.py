head = [0, 0]
tail = [0, 0]

visited = {(0, 0)}
with open(0) as f:
	for line in f:
		if line[0] == 'R':
			for i in range(int(line[2:])):
				head[0] += 1
				if tail[0] < head[0] - 1:
					tail = [head[0] - 1, head[1]]
				visited.add(tuple(tail))
		elif line[0] == 'L':
			for i in range(int(line[2:])):
				head[0] -= 1
				if tail[0] > head[0] + 1:
					tail = [head[0] + 1, head[1]]
				visited.add(tuple(tail))
		elif line[0] == 'U':
			for i in range(int(line[2:])):
				head[1] += 1
				if tail[1] < head[1] - 1:
					tail = [head[0], head[1] - 1]
				visited.add(tuple(tail))
		elif line[0] == 'D':
			for i in range(int(line[2:])):
				head[1] -= 1
				if tail[1] > head[1] + 1:
					tail = [head[0], head[1] + 1]
				visited.add(tuple(tail))

print(len(visited))