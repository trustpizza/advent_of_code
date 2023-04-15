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

# def find_list_size(lines):
#     up_and_down_inputs = list(filter(lambda item: item is not None, map(lambda line: line if (line[0] == "U" or line[0] == "D") else None, lines)))
#     left_and_right_inputs = list(filter(lambda item: item is not None, map(lambda line: line if line[0] == "R" or line[0] == "L" else None, lines)))
    
#     # print(up_and_down_inputs)
#     # print(max_height)
#     # print(left_and_right_inputs)

#     return [[" " for i in range(max_width)] for i in range(max_height)]# * max_height

def part_one(file):
    data = parse_inputs(file)
    # bridge = RopeBridge(data)
    
    # for line in data:
        # bridge.process_movement(line)
    # bridge.show_bridge()

    return 

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