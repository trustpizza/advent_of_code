import os

def part_one(file_name):
    score = 0
    combos = process_rps(file_name)
    for game in combos:
        game = list(game)
        p1val = game[0]
        p2val = game[1]

    return

def part_two():
    return

# 1 is Rock
# 2 is Paper
# 3 is Scissors

# true is a win
# false is a loss
def rocks_paper_scissors(val1, val2):
    if (val1 == val2):
        return 3
    elif (val1 == 1): 
        if (val2 == 2):
            return 6
        else:
            return 0
    elif (val1 == 2): 
        if (val2 == 1):
            return 0
        elif (val2 == 3):
            return 6
    elif (val1 == 3): 
        if (val2 == 1):
            return 6
        elif (val2 == 2):
            return 0

def convert_value_to_rps(val):
    if (val == "X" or val == "A"):
        return 1
    elif (val == "Y" or val == "B"):
        return 2
    elif (val == "Z" or val == "C"):
        return 3

def process_rps(file_name):
    with open(file_name) as f:
        combos = f.read()

    combos = combos.split()
    combos = ["".join(x) for x in zip(combos[0::2], combos[1::2])]

    return combos

if __name__ == "__main__":
    file_dir = os.path.dirname(os.path.realpath("__file__"))
    input_file = "temp.txt" #temp is the small test file
    file_name = os.path.join(file_dir, input_file)

    print("---Part One---")
    print(part_one(file_name))
    #print("---Part Two---")
    #print(part_two(file_name))