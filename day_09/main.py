class Knot:
    def __init__(self, location: list, child = None, parent = None) -> None:
        self.location = location
        self.was_diag = False
        self.child = child

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

    def set_diag_false(self):
        self.was_diag = False

    def set_diag_true(self):
        self.was_diag = True

    def set_child(self, child):
        self.child = child

def check_rope_is_touching(head_loc, tail_loc):
    if tail_loc[0] >= head_loc[0]-1 and tail_loc[0] <= head_loc[0] +1 and tail_loc[1] >= head_loc[1] -1 and tail_loc[1] <= head_loc[1] +1:
        return True
    else:   
        return False

def is_diagnol(head_loc,tail_loc):
    if (tail_loc[0] == head_loc[0]+1 or tail_loc[0] == head_loc[0]-1) and (tail_loc[1] == head_loc[1]-1 or tail_loc[1] == head_loc[1]+1):
        return True
    else:
        return False


def part_one(file):
    data = parse_inputs(file)
    
    tail = Knot([0,0])
    head = Knot([0,0], tail)

    locations = []
    # was_diag = False 

    for line in data:
        for _ in range(line[1]):
            head_loc = list(head.get_loc())
            head.move(line[0])

            if tail.was_diag and not check_rope_is_touching(head.get_loc(), tail.get_loc()): # Valid move
                tail.set_loc(head_loc)
    
            tail.set_diag_false()

            if is_diagnol(head.get_loc(),tail.get_loc()): # Prepare for the next move
                tail.set_diag_true()  

            if not check_rope_is_touching(head.get_loc(),tail.get_loc()): # Move the tail for normal diaganols
                tail.move(line[0])

            locations.append(list(tail.get_loc()))

    out = set(tuple(loc) for loc in locations)
    return len(out)

def part_two(file):
    data = parse_inputs(file)

    knots = []
    for _ in range(4): # Create and populate Knots list
        knot = Knot([0,0])
        knots.append(knot)

    for i in range(len(knots)):
        if i < len(knots)-1:
            knots[i].set_child(knots[i+1])

    locations = []

    for line in data:
        for _ in range(line[1]):
            for i in range(len(knots)):
                head = knots[i]
                tail = head.child
                if tail: 
                    head_loc = list(head.get_loc())
                    head.move(line[0])

                    if tail.was_diag and not check_rope_is_touching(head.get_loc(), tail.get_loc()): # Valid move
                        tail.set_loc(head_loc)
            
                    tail.set_diag_false()

                    if is_diagnol(head.get_loc(),tail.get_loc()): # Prepare for the next move
                        tail.set_diag_true()  

                    if not check_rope_is_touching(head.get_loc(),tail.get_loc()): # Move the tail for normal diaganols
                        tail.move(line[0])
                    
                    if tail.child == None:
                        locations.append(list(tail.get_loc()))
                    
                    print(knots[0].get_loc(), knots[1].get_loc(), knots[2].get_loc(), knots[3].get_loc())

    out = set(tuple(loc) for loc in locations)

    print(locations)
    return len(out)

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