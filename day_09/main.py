class Piece:
    def __init__(self, location: list) -> None:
        self.location = location

    def move(self,direction) -> None:
        if direction == "U":
            self.location[1] += 1
        elif direction == "D":
            self.location[1] -= 1
        elif direction == "R":
            self.location[0] += 1
        elif direction == "L":
            self.location[0] -= 1

    def set_loc(self, location: list) -> None:
        self.location = location

    def get_loc(self) -> list:
        return self.location


def check_rope_is_touching(head_loc, tail_loc):
    if tail_loc[0] >= head_loc[0]-1 and tail_loc[0] <= head_loc[0] +1 and tail_loc[1] >= head_loc[1] -1 and tail_loc[1] <= head_loc[1] +1:
        return True
    else:   
        return False

def is_diagnol(head_loc,tail_loc):
    if (tail_loc[0] == head_loc[0]+1 or tail_loc[0] == head_loc[0]-1) and (tail_loc[1] == head_loc[1]-1 or tail_loc[1] == head_loc[1]+1):
        return True

def part_one(file):
    data = parse_inputs(file)
    # up_and_down_inputs = list(filter(lambda item: item is not None, map(lambda line: line if (line[0] == "U" or line[0] == "D") else None, lines)))
    # left_and_right_inputs = list(filter(lambda item: item is not None, map(lambda line: line if line[0] == "R" or line[0] == "L" else None, lines)))

    head = Piece([0,0])
    tail = Piece([0,0])

    locations = []
    was_diag = False 

    for line in data:
        for _ in range(line[1]):
            head_loc = list(head.get_loc())
            head.move(line[0])

            if was_diag and not check_rope_is_touching(head.get_loc(), tail.get_loc()): # Valid move
                tail.set_loc([head_loc[0], head_loc[1]])
    
            was_diag = False

            if is_diagnol(head.get_loc(),tail.get_loc()): # Prepare for the next move
                was_diag = True  

            if not check_rope_is_touching(head.get_loc(),tail.get_loc()): # Move the tail for normal diaganols
                tail.move(line[0])

            locations.append(list(tail.get_loc()))

    out = set(tuple(loc) for loc in locations)
    return len(out)

def part_two(file):
    """
    Plan:
        I could create 10 seperate pieces and set each as a 'head' to the one behind it, starting with the true head and ending with the tail
        Let's try???
    """
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
    input_file = "input.txt"
    print("---Part One---")
    print(part_one(input_file))
    print("---Part Two---")
    print(part_two(input_file))