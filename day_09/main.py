class Piece:
    def __init__(self, location: list) -> None:
        self.location = location

    def move(self,direction) -> None:
        if direction == "U":
            self.location[0] += 1
        elif direction == "D":
            self.location[0] -= 1
        elif direction == "R":
            self.location[1] += 1
        elif direction == "L":
            self.location[1] -= 1

    def get_loc(self) -> list:
        return self.location

def check_rope_is_touching(head, tail):
    head_loc = head.get_loc()
    tail_loc = tail.get_loc()

    if tail_loc[0] >= head_loc[0]-1 and tail_loc[0] <= head_loc[0] +1 and tail_loc[1] >= head_loc[1] -1 and tail_loc[1] <= head_loc[1] +1:
        return True
    else:
        return False

def part_one(file):
    data = parse_inputs(file)
    # up_and_down_inputs = list(filter(lambda item: item is not None, map(lambda line: line if (line[0] == "U" or line[0] == "D") else None, lines)))
    # left_and_right_inputs = list(filter(lambda item: item is not None, map(lambda line: line if line[0] == "R" or line[0] == "L" else None, lines)))

    head = Piece([0,0])
    tail = Piece([0,0])

    locations = []

    for line in data:
        for _ in range(line[1]):
            head.move(line[0])
            is_touching = check_rope_is_touching(head, tail)
            
            if not is_touching:
                tail.move(line[0])
            current_location = tail.get_loc()

            print(head.get_loc(), tail.get_loc())            
            # Find all moves  
            locations.append([current_location[0], current_location[1]])
    # print(locations)
    out = set(tuple(loc) for loc in locations)
    return len(out)

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