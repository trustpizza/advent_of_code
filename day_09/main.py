def part_one(file):
    data = parse_inputs(file)
    print(data)

def part_two(file):
    return

def clean_input_line(line) -> None:
    line = line.split(" ")
    line[1] = int(line[1])
    return line

def parse_inputs(file):
    with open(file) as f:
        lines = f.read().splitlines()
        lines = list(map(clean_input_line, lines))
    return lines

if __name__ == "__main__":
    input_file = "temp.txt"
    print("---Part One---")
    print(part_one(input_file))
    print("---Part Two---")
    print(part_two(input_file))