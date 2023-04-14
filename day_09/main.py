class RopeBridge:
    def __init__(self, lines) -> None:
        self.bridge = find_list_size(lines)
        self.tail = self.bridge[0][0] = "T"
        self.head = self.bridge[0][0] = "H"

    def show_bridge(self):
        print(self.bridge)

    def move_head(direction, spaces):
        pass

def determine_max(lines):
    max_location = 0
    current_location = 0

    for line in lines:
        if line[0] == "U" or line[0] == "R":
            current_location += line[1]
        else:
            current_location -= line[1]
        if current_location > max_location: max_location = current_location
    return max_location

def find_list_size(lines):
    up_and_down_inputs = list(filter(lambda item: item is not None, map(lambda line: line if (line[0] == "U" or line[0] == "D") else None, lines)))
    left_and_right_inputs = list(filter(lambda item: item is not None, map(lambda line: line if line[0] == "R" or line[0] == "L" else None, lines)))
    
    # print(up_and_down_inputs)
    max_height = determine_max(up_and_down_inputs)
    # print(max_height)
    # print(left_and_right_inputs)
    max_width = determine_max(left_and_right_inputs)

    return [[None for i in range(max_width)] for i in range(max_height)]# * max_height

def part_one(file):
    data = parse_inputs(file)
    bridge = RopeBridge(data)

    return bridge

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