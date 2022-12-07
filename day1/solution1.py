import sys


def get_groups(filepath):
	with open(filepath) as f:
		str_groups = open(filepath).read().split('\n\n')
		int_groups = [list(map(int, s_g.split('\n'))) for s_g in str_groups]
	return int_groups


def main():
	groups = get_groups(sys.argv[1])
	max_sum = -1
	for group in groups:
		max_sum = max(max_sum, sum(group))
	print(max_sum)


if __name__ == '__main__':
	main()