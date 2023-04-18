class Knot:
    def __init__(self, location: list, child = None, parent = None) -> None:
        self.location = location
        self.was_diag = False
        self.child = child
        self.parent = parent

    def move(self,direction) -> None:
        loc = list(self.get_loc())
        if direction == "U":
            self.location[1] += 1
        elif direction == "D":
            self.location[1] -= 1
        elif direction == "R":
            self.location[0] += 1
        elif direction == "L":
            self.location[0] -= 1
        self.__update_child(self.child, direction, loc)#self, self.child, direction)

    def __update_child(self, child, direction,loc):#self, child, direction):
        if self.child != None:
            if child.was_diag and not check_rope_is_touching(list(self.get_loc()), child.get_loc()): # Valid move
            #     print(child.get_loc(), "Diag")
                child.set_loc(loc)
                # child.__update_child(child.child, direction, loc)

            # child.set_diag_false()
            self.check_diag()

            if not check_rope_is_touching(self.get_loc(),child.get_loc()): # Move the tail for normal diaganols
                child.move(direction)
                # print(child.get_loc(), "Not Touching")

    def set_loc(self, location: list, direction = None) -> None:
        old_loc = list(self.get_loc())
        self.location = location
        if self.child!= None:
            self.child.set_loc(old_loc)
        # self.__update_child(self.child, direction, location)

    def get_loc(self) -> list:
        return self.location

    def set_diag_false(self):
        self.was_diag = False

    def set_diag_true(self):
        self.was_diag = True

    def check_diag(self):
        # parent = self.parent
        child = self.child
        if is_diagnol(list(self.get_loc()), list(child.get_loc())):
            child.set_diag_true()
        if child.child != None: child.check_diag()

    def set_child(self, child):
        self.child = child

    def set_parent(self, parent):
        self.parent = parent

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

def move_knot(knots, current_knot_idx, prior_knot, next_knot, line):
    # print(current_knot_idx)
    current_knot = None
    print
    if current_knot_idx < len(knots) -1: 
        current_knot = knots[current_knot_idx]
        current_knot.move(line[0])

        if current_knot == knots[0]:
            print()
            move_knot(knots, current_knot_idx= current_knot_idx+1, prior_knot=current_knot, next_knot = knots[current_knot_idx+2])
        else:
            print("not head")
            if not knots[-1] == current_knot:
                current_loc = list(current_knot.get_loc())
                # is current_knot touching prior_knot?
                print(check_rope_is_touching(current_knot.get_loc(), prior_knot.get_loc()))
            move_knot(knots, current_knot_idx= current_knot_idx+1, prior_knot=current_knot, next_knot = knots[current_knot_idx+2])
    else: return

    print(current_knot.get_loc())
    """
    Move the knot

    Until we are moving the tail, check if the current_knot is touching the prior_knot    
    """
    
    pass

def move_rope(knots, idx, line):
    head = knots[0]
    tail = knots[-1]
    # print(head, middle_knots, tail)
    """
    Every time there is a line, we move the head.
    
    If we move the head, look through each of the middle pieces of the rope
        Take the middle knot
        Look for the next knot, if there is none set that to be the tail

        Look for the prior knot, if there is none, set that to the head

        If the prior knot is not touching:
            

    # """
    head.move(line[0])
    print(knots[0].get_loc(),knots[1].get_loc(), knots[2].get_loc(), knots[-1].get_loc())

    return
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
            return(list(tail.get_loc()))

    

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

    for i in range(len(knots)):
        if i != 0:
            knots[i].set_parent(knots[i-1])

    locations = []

    for line in data:
        for _ in range(line[1]):
            # for i in range(len(knots)):
            location = move_rope(knots, i, line)
                # print(location)
                # head = knots[i]
                # parent = head.parent
                # tail = head.child

            """
                Currently what happens is if there is a tail, the head moves.
                If the tail meets all of the conditions(it wasn't diaganol, it's not touching)
                    The tail is updated to the head location
                if the tail is now diaganol,
                
            """
                # if tail:
                #     if parent != None: # Case of the head
                #         head_loc = list(head.get_loc())
                #         head.move(line[0])


                #     else:
                #         head_loc = list(head.get_loc())
                #         head.move(line[0])

                #         if tail.was_diag and not check_rope_is_touching(head.get_loc(), tail.get_loc()): # Valid move
                #             tail.set_loc(head_loc)
                
                #         tail.set_diag_false()

                #         if is_diagnol(head.get_loc(),tail.get_loc()): # Prepare for the next move
                #             tail.set_diag_true()  

                #         if not check_rope_is_touching(head.get_loc(),tail.get_loc()): # Move the tail for normal diaganols
                #             tail.move(line[0])
                        
                #         if tail.child == None:
                #             locations.append(list(tail.get_loc()))
                        
                #     print(knots[0].get_loc(), knots[1].get_loc(), knots[2].get_loc(), knots[3].get_loc())

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