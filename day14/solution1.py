
cave = set()
floor = 0
with open(0) as f:
	for line in f:
		coords = [tuple(coordstr.split(',')) for coordstr in line.split(' -> ')]
		coords = [(int(first), int(second)) for first, second in coords]

		for i in range(len(coords) - 1):
			first = coords[i]
			second = coords[i+1]
			if first[0] == second[0]:
				if first[1] > second[1]:
					first, second = (second, first)
				for y in range(first[1], second[1] + 1):
					cave.add((first[0], y))
			elif first[1] == second[1]:
				if first[0] > second[0]:
					first, second = (second, first)
				for x in range(first[0], second[0] + 1):
					cave.add((x, first[1]))
			floor = max(floor, second[1])

orig_cave_size = len(cave)
source = (500, 0)

sand = source
while sand[1] < floor:
	if (sand[0], sand[1]+1) not in cave:
		sand = (sand[0], sand[1]+1)
	elif (sand[0]-1, sand[1]+1) not in cave:
		sand = (sand[0]-1, sand[1]+1)
	elif (sand[0]+1, sand[1]+1) not in cave:
		sand = (sand[0]+1, sand[1]+1)
	else:
		cave.add(sand)
		sand = source

final_cave_size = len(cave)
print(final_cave_size - orig_cave_size)