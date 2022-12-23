import sys

OPPONENT_ROCK = 'A' 
OPPONENT_PAPER = 'B'
OPPONENT_SCISSORS = 'C'

PLAYER_ROCK = 'X'
PLAYER_PAPER = 'Y'
PLAYER_SCISSORS = 'Z'

round_points = {
	(OPPONENT_ROCK, PLAYER_ROCK): 4,
	(OPPONENT_PAPER, PLAYER_ROCK): 1,
	(OPPONENT_SCISSORS, PLAYER_ROCK): 7,
	(OPPONENT_ROCK, PLAYER_PAPER): 8,
	(OPPONENT_PAPER, PLAYER_PAPER): 5,
	(OPPONENT_SCISSORS, PLAYER_PAPER): 2,
	(OPPONENT_ROCK, PLAYER_SCISSORS): 3,
	(OPPONENT_PAPER, PLAYER_SCISSORS): 9,
	(OPPONENT_SCISSORS, PLAYER_SCISSORS): 6
}


def get_rounds(filepath):
	with open(filepath) as f:
		return [tuple(line.strip().split(' ')) for line in f]


def main():
	rounds = get_rounds(sys.argv[1])
	total = sum([round_points.get(round) for round in rounds])
	print(total)


if __name__ == '__main__':
	main()
