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


pairs = []
with open(0) as f:
	while True:
		left = next(f).strip()
		right = next(f).strip()
		pairs.append((ast.literal_eval(left), ast.literal_eval(right)))
		try:
			next(f)
		except:
			break

result = 0
for i, pair in enumerate(pairs):
	if compare_values(pair[0], pair[1]) == RIGHT_ORDER:
		result += (i + 1)

print(result)