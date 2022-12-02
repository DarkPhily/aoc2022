
ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = 0
DRAW = 3
WIN = 6


def check_outcome(round):
    opponent, myself = round.split()
    if opponent == 'A':
        if myself == 'X':
            return DRAW + ROCK
        if myself == 'Y':
            return WIN + PAPER
        if myself == 'Z':
            return LOSE + SCISSORS
    elif opponent == 'B':
        if myself == 'X':
            return LOSE + ROCK
        if myself == 'Y':
            return DRAW + PAPER
        if myself == 'Z':
            return WIN + SCISSORS
    elif opponent == 'C':
        if myself == 'X':
            return WIN + ROCK
        if myself == 'Y':
            return LOSE + PAPER
        if myself == 'Z':
            return DRAW + SCISSORS


points = []

with open("./data.txt", 'r') as data:
    points.extend(check_outcome(line) for line in data)

# Solution 1
print(f"Answer 1: {sum(points)}")


def check_gesture(round):
    opponent, myself = round.split()
    if myself == 'X':  # LOSE
        if opponent == 'A':
            return SCISSORS + LOSE
        if opponent == 'B':
            return ROCK + LOSE
        if opponent == 'C':
            return PAPER + LOSE
    elif myself == 'Y':  # DRAW
        if opponent == 'A':
            return ROCK + DRAW
        if opponent == 'B':
            return PAPER + DRAW
        if opponent == 'C':
            return SCISSORS + DRAW
    elif myself == 'Z':  #  WIN
        if opponent == 'A':
            return PAPER + WIN
        if opponent == 'B':
            return SCISSORS + WIN
        if opponent == 'C':
            return ROCK + WIN


points = []
with open("./data.txt", 'r') as data:
    points.extend(check_gesture(line) for line in data)

print(f"Answer 2: {sum(points)}")
