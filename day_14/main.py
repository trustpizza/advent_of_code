def part_one(file):
    lines = parse_inputs(file)
    print(lines)
    # First draw rock positions
    pass


def parse_inputs(file):
    with open(file, "r", encoding="utf-8") as f:
        # lines = f.read().splitlines()
        lines = list(map(lambda line: list(map(lambda entry: tuple(map(lambda input_half: int(input_half), entry.split(","))), line)), [line.split(" -> ") for line in f.read().splitlines()]))
    return lines


if __name__ == "__main__":
    filename = 'temp.txt'
    print("---Part One---")
print(part_one(filename))