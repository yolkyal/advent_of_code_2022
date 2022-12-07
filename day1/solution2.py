import sys


def get_groups(filepath):
	with open(filepath) as f:
		str_groups = open(filepath).read().split('\n\n')
		int_groups = [list(map(int, s_g.split('\n'))) for s_g in str_groups]
	return int_groups


def main():
	groups = get_groups(sys.argv[1])
	max_sum = -1
	group_totals = list(map(sum, groups))
	top_three_total = sum(sorted(group_totals)[-3:])
	print(top_three_total)


if __name__ == '__main__':
	main()