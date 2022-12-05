import sys


def get_all_contents(filepath):
	with open(filepath) as f:
		return [line.strip() for line in f]


def get_repeated_item(contents):
	first = contents[:len(contents) // 2]
	second = contents[len(contents) // 2:]
	for char in first:
		if char in second:
			return char


def get_priority(char):
	return (ord(char) - 96) if char.islower() else (ord(char) - 38)


def main():
	ls_contents = get_all_contents(sys.argv[1])
	result = sum([get_priority(get_repeated_item(contents)) for contents in ls_contents])
	print(result)


if __name__ == '__main__':
	main()
