class Monkey:
	def __init__(self, items, operation_str, test_div, true_monkey, false_monkey):
		self.items = items
		self.operation_str = operation_str
		self.test_div = test_div
		self.true_monkey = true_monkey
		self.false_monkey = false_monkey
		self.inspections = 0

	def __repr__(self):
		return str(self.items)


monkeys = []
with open(0) as f:
	while True:
		try:
			next(f) # Monkey num
			items = list(map(int, next(f).strip().replace('Starting items: ', '').split(',')))
			operation_str = next(f).strip().replace('Operation: ', '').replace('old', 'item')
			test_div = int(next(f).strip().replace('Test: divisible by ', ''))
			true_monkey = int(next(f).strip().replace('If true: throw to monkey ', ''))
			false_monkey = int(next(f).strip().replace('If false: throw to monkey ', ''))
			monkeys.append(Monkey(items, operation_str, test_div, true_monkey, false_monkey))
			next(f) # Blank line
		except:
			break

mult_div = 1
for monkey in monkeys:
	mult_div *= monkey.test_div

for i in range(10000):
	for monkey in monkeys:
		for item in monkey.items:
			monkey.inspections += 1
			exec(monkey.operation_str)

			new %= mult_div
			if new % monkey.test_div == 0:
				monkeys[monkey.true_monkey].items.append(new)
			else:
				monkeys[monkey.false_monkey].items.append(new)
		monkey.items = []


inspections = [monkey.inspections for monkey in monkeys]
max_ins1, max_ins2 = sorted(inspections)[-2:]
print(max_ins1 * max_ins2)
