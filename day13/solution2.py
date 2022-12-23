import ast

RIGHT_ORDER = 1
WRONG_ORDER = -1
CONTINUE = 0


def compare_values(left, right):
	types = (type(left), type(right))

	if type(left) == int and type(right) == int:
		if left < right:
			return RIGHT_ORDER
		elif left > right:
			return WRONG_ORDER
		else:
			return CONTINUE

	if type(left) == list and type(right) == list:
		for i in range(len(left)):
			if i > len(right) - 1:
				return WRONG_ORDER
			comparison = compare_values(left[i], right[i])
			if comparison != CONTINUE:
				return comparison
		if len(left) < len(right):
			return RIGHT_ORDER
		else:
			return CONTINUE

	if type(left) == int:
		left = [left]
	elif type(right) == int:
		right = [right]

	return compare_values(left, right)


packets = []
with open(0) as f:
	while True:
		left = next(f).strip()
		right = next(f).strip()
		packets.append(ast.literal_eval(left))
		packets.append(ast.literal_eval(right))
		try:
			next(f)
		except:
			break

first_div_index, second_div_index = 1, 2
first_divider, second_divider = [[2]], [[6]]
for packet in packets:
	if compare_values(packet, first_divider) == RIGHT_ORDER:
		first_div_index += 1
	if compare_values(packet, second_divider) == RIGHT_ORDER:
		second_div_index += 1

print(first_div_index * second_div_index)