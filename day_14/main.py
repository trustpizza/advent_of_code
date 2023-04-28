def part_one(file):
    lines = parse_inputs(file)
    for line in lines:
        for idx in range(len(line)):
            if idx < len(line) - 1:
                find_rocks(line[idx], line[idx+1])
    # First draw rock positions
    print(lines)
    pass


def find_rocks(first_pos, second_pos):
    if first_pos[0] - second_pos[0] == 0:
        for i in range(abs(first_pos[1]-second_pos[1]) + 1):
            rock = (first_pos[0], first_pos[1]+i)
            print(rock)
    else:
        for i in range(abs(first_pos[0]-second_pos[0]) +1):
            rock = (first_pos[0]+i, first_pos[1])
            print(rock)
    # Take a line
        # Take the first two tuples
        # Subtract the first items of both, if == 0, Rock is moving on the X axis
            # Return Tuples STarting with the First, Ending with the Last, and with all in between
        # Else the Rocks are moving on the Y axis
    


def parse_inputs(file):
    with open(file, "r", encoding="utf-8") as f:
        lines = list(map(lambda line: list(map(lambda entry: tuple(map(lambda input_half: int(input_half), entry.split(","))), line)), [line.split(" -> ") for line in f.read().splitlines()]))
    return lines


if __name__ == "__main__":
    filename = 'temp.txt'
    print("---Part One---")
    print(part_one(filename))