import sys


def get_assignments(filepath):
	with open(filepath) as f:
		assignments = []
		for line in f:
			pairs = line.strip().split(',')
			first_nums = list(map(int, pairs[0].split('-')))
			second_nums = list(map(int, pairs[1].split('-')))
			assignments.append(tuple([first_nums[0], first_nums[1], second_nums[0], second_nums[1]]))
		return assignments


def is_fully_contained(a):
	return (a[0] <= a[2] and a[1] >= a[3]) or (a[0] >= a[2] and a[1] <= a[3])


def main():
	assignments = get_assignments(sys.argv[1])
	result = sum([is_fully_contained(a) for a in assignments])
	print(result)


if __name__ == '__main__':
	main()
