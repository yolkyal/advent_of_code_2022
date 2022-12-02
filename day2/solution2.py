import sys

OPPONENT_ROCK = 'A'
OPPONENT_PAPER = 'B'
OPPONENT_SCISSORS = 'C'

NEED_TO_LOSE = 'X'
NEED_TO_DRAW = 'Y'
NEED_TO_WIN = 'Z'

ROCK_LOSS = 1
PAPER_LOSS = 2
SCISSORS_LOSS = 3
ROCK_DRAW = 4
PAPER_DRAW = 5
SCISSORS_DRAW = 6
ROCK_WIN = 7
PAPER_WIN = 8
SCISSORS_WIN = 9


round_points = {
	(OPPONENT_ROCK, NEED_TO_LOSE): SCISSORS_LOSS,
	(OPPONENT_PAPER, NEED_TO_LOSE): ROCK_LOSS,
	(OPPONENT_SCISSORS, NEED_TO_LOSE): PAPER_LOSS,
	(OPPONENT_ROCK, NEED_TO_DRAW): ROCK_DRAW,
	(OPPONENT_PAPER, NEED_TO_DRAW): PAPER_DRAW,
	(OPPONENT_SCISSORS, NEED_TO_DRAW): SCISSORS_DRAW,
	(OPPONENT_ROCK, NEED_TO_WIN): PAPER_WIN,
	(OPPONENT_PAPER, NEED_TO_WIN): SCISSORS_WIN,
	(OPPONENT_SCISSORS, NEED_TO_WIN): ROCK_WIN
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