def determine_width(lines):
    pass

def determine_height(lines):
    pass

def find_list_size(lines):
    up_and_down_inputs = list(filter(lambda item: item is not None, map(lambda line: line if (line[0] == "U" or line[0] == "D") else None, lines)))
    left_and_right_inputs = list(filter(lambda item: item is not None, map(lambda line: line if line[0] == "R" or line[0] == "L" else None, lines)))
    print(up_and_down_inputs)
    print(left_and_right_inputs)

def part_one(file):
    data = parse_inputs(file)
    find_list_size(data)
    return data

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