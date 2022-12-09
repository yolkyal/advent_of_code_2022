rope = [[0, 0] for i in range(10)]#


def is_touching(first, second):
	return abs(first[0] - second[0]) < 2 and abs(first[1] - second[1]) < 2


def update_rope():
	global rope
	for i in range(1, 10):
		if not is_touching(rope[i], rope[i-1]):
			if rope[i][0] < rope[i-1][0]:
				rope[i][0] += 1
			elif rope[i][0] > rope[i-1][0]:
				rope[i][0] -= 1
			if rope[i][1] < rope[i-1][1]:
				rope[i][1] += 1
			elif rope[i][1] > rope[i-1][1]:
				rope[i][1] -= 1


visited = {(0, 0)}
with open(0) as f:
	for line in f:
		if line[0] == 'R':
			for i in range(int(line[2:])):
				rope[0][0] += 1
				update_rope()
				visited.add(tuple(rope[9]))
		elif line[0] == 'L':
			for i in range(int(line[2:])):
				rope[0][0] -= 1
				update_rope()
				visited.add(tuple(rope[9]))
		elif line[0] == 'U':
			for i in range(int(line[2:])):
				rope[0][1] += 1
				update_rope()
				visited.add(tuple(rope[9]))
		elif line[0] == 'D':
			for i in range(int(line[2:])):
				rope[0][1] -= 1
				update_rope()
				visited.add(tuple(rope[9]))


print(len(visited))