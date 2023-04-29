from functools import reduce
from operator import concat

def part_one(file):
    lines = parse_inputs(file)

    rocks = []
    for line in lines:
        for idx in range(len(line)):
            if idx < len(line) - 1:
                rock_row = find_rocks(line[idx], line[idx+1])
                rocks.append(rock_row)
    rocks = set(list(reduce(concat, rocks))) #Creates a set to remove additional values in a flattened list
    # Find bottom_most edge closest to the
    origin = (500,0) 
    sand_locations = place_sand(origin, rocks, list(origin))
    return sand_locations


def place_sand(origin, rocks, current_position, sand_locations=[]):
    if not look_left(current_position, rocks, sand_locations) and not look_right(current_position, rocks, sand_locations):
        return sand_locations

    current_position = find_bottom(current_position, rocks, sand_locations)
    sand_locations.append(current_position) # This adds the first one to start things off

    if len(sand_locations) > 5:
        print(sand_locations)
        return 

    if not lookout_below(current_position, rocks, sand_locations): #Stops when the pile reaches the origin
        current_position = find_bottom(current_position, rocks, sand_locations)

        # left = [current_position[0], current_position[1]]
        right = tuple(current_position)

        while bool(look_left(left, rocks, sand_locations)): #Triggered when you can look left and find an empty space
            left = look_left(current_position, rocks, sand_locations)
            sand_locations.append(left)

            # if bool(look_right(current_position, rocks, sand_locations)):
            #     pass
            # else:

        else:
            sand_locations.append(current_position)

        current_position = find_bottom(current_position, rocks, sand_locations)
        place_sand(origin, rocks, current_position, sand_locations)
    else:
        return


    # Stop when look down, look left, or look right is the edge STOP and return sand_locations!

    # First look down until 
    # if down is occupied, look left
        # if left is occupied, look right
            # if right is occupied, do nothing
            # else add the right location to the sand_locations, rerun...
        # If it isn't, add the left location to the sand_locations, rerun...

    # If it isn't, add the down location to the sand_locations, rerun place_sand with origin, rocks, sandlocations 
    return     
    

def find_bottom(position,rocks, sand_locations):
    next_location = (position[0], position[1])

    while next_location not in rocks and next_location not in sand_locations:
        next_location = (next_location[0], next_location[1]+1)
    
    return (next_location[0], next_location[1]-1)


def lookout_below(position, rocks, sand_locations):
    below = (position[0], position[1]+1)
    if below not in rocks and below not in sand_locations:
        return below
    else: 
        return False

    
def look_left(position, rocks, sand_locations):
    left = (position[0]-1, position[1]+1)
    if left not in rocks and left not in sand_locations:
        return left
    else: 
        return False


def look_right(position, rocks, sand_locations):
    right = (position[0]+1, position[1]+1)
    if right not in rocks and right not in sand_locations:
        return right
    else: return False


def find_rocks(first_pos, second_pos):
    rock_row = []
    if first_pos[0] - second_pos[0] == 0:
        for i in range(abs(first_pos[1]-second_pos[1]) + 1):
            rock = vertical_rock(first_pos, second_pos, i)
            rock_row.append(rock)
    else:
        for i in range(abs(first_pos[0]-second_pos[0]) + 1):
            rock = horizontal_rock(first_pos, second_pos, i)
            rock_row.append(rock)
    return rock_row


def vertical_rock(first_pos, second_pos, i):
    if first_pos[1] - second_pos [1] > 0:
        rock = (first_pos[0], first_pos[1]-i)
    else:
        rock = (first_pos[0], first_pos[1]+i)
    return rock


def horizontal_rock(first_pos, second_pos, i):
    if first_pos[0] - second_pos[0] > 0:
        rock = (first_pos[0]-i, first_pos[1])
    else:
        rock = (first_pos[0]+i, first_pos[1])
    return rock


def parse_inputs(file):
    with open(file, "r", encoding="utf-8") as f:
        lines = list(map(lambda line: list(map(lambda entry: tuple(map(lambda input_half: int(input_half), entry.split(","))), line)), [line.split(" -> ") for line in f.read().splitlines()]))
    return lines


if __name__ == "__main__":
    filename = 'temp.txt'
    print("---Part One---")
    print(part_one(filename))