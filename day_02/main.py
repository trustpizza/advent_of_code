import os
from enum import Enum, auto

class Move(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

    def beats(self):
        match self:
            case Move.ROCK:
                return Move.SCISSORS
            case Move.PAPER:
                return Move.ROCK
            case Move.SCISSORS:
                return Move.PAPER

    def loses_to(self):
        match self:
            case Move.ROCK:
                return Move.PAPER
            case Move.PAPER:
                return Move.SCISSORS
            case Move.SCISSORS:
                return Move.ROCK

    def move_score(self):
        match self:
            case Move.ROCK:
                return 1
            case Move.PAPER:
                return 2
            case Move.SCISSORS:
                return 3

    @classmethod
    def to_move(cls, move: str):
        match move:
            case "A" | "X":
                return Move.ROCK
            case "B" | "Y":
                return Move.PAPER
            case "C" | "Z":
                return Move.SCISSORS
        raise ValueError("Invalid move")

def calc_game_score(opp_move, my_move: Move):
    if opp_move == my_move:
        return 3
    elif my_move == opp_move.loses_to(): #Win Case
        return 6
    elif my_move == opp_move.beats():
        return 0

def convert_letter_to_rps(char):
    if (char == "A" or char == "X"):
        return 1
    elif (char == "B" or char == "Y"):
        return 2
    elif (char == "C" or char == "Z"):
        return 3

def read_file(file_name):
    with open(file_name) as f:
        combos = f.read()

    combos = combos.split()
    combos = ["".join(x) for x in zip(combos[0::2], combos[1::2])]
    
    return combos

def part_one(file):
    total_score = 0

    combos = read_file(file)
    for game in combos:
        opp_move, my_move = Move.to_move(game[0]), Move.to_move(game[1])
        total_score += my_move.move_score()
        total_score += calc_game_score(opp_move, my_move)

    return total_score

def part_two(file):
    total_score = 0

    combos = read_file(file)
    for move, outcome in combos:
        opp_move = Move.to_move(move)
        match outcome:
            case "X": # Lose
                my_move = opp_move.beats()
            case "Y": # Tie
                my_move = opp_move
            case "Z": #win
                my_move = opp_move.loses_to()

        total_score += my_move.move_score()
        total_score += calc_game_score(opp_move, my_move)
    return total_score

if __name__ == "__main__":
    file_dir = os.path.dirname(os.path.realpath("__file__"))
    input_file = "input.txt" #temp is the small test file
    file_name = os.path.join(file_dir, input_file)
    print("---Part One---")
    print(part_one(file_name))
    print("---Part Two---")
    print(part_two(file_name))