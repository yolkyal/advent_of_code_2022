import sys


def get_all_groups(filepath):
	groups = []
	with open(filepath) as f:
		while True:
			try:
				group = [next(f).strip(), next(f).strip(), next(f).strip()]
			except:
				return groups
			groups.append(group)


def get_common_item(group):
	for item in group[0]:
		if item in group[1] and item in group[2]:
			return item


def get_priority(char):
	return (ord(char) - 96) if char.islower() else (ord(char) - 38)


def main():
	ls_groups = get_all_groups(sys.argv[1])
	result = sum([get_priority(get_common_item(group)) for group in ls_groups])
	print(result)


if __name__ == '__main__':
	main()
