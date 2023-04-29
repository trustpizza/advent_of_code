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

    sand = []
    for i in range(23):
        try:
            sand = drop_sand(origin, rocks, sand)
        except:
            print(len(sand))

    # Now I need to create a way to loop appropriately and call the end.  
    # draw(sand, rocks)
    return


def drop_sand(grain: tuple, rocks: set, sand=[]) -> tuple:
    next_grain = check_down(grain, rocks, sand) # First the grain drops down
    
    if not is_empty((grain[0]-1, grain[1]+1), rocks, sand): # Looking left
        old_grain = tuple(next_grain)
        
        next_grain = check_left(old_grain, rocks, sand)
        if not is_empty((next_grain[0]+1, next_grain[1]+1), rocks, sand): # Looking right
            next_grain = check_right(old_grain, rocks, sand)
    
    sand.append(next_grain)

    # Print if the old grain == the grain
    print(next_grain)
    return sand


def check_down(grain: tuple, rocks: set, sand: list):
    if is_empty((grain[0], grain[1]+1), rocks, sand):
        return grain

    return check_down((grain[0],grain[1]+1), rocks, sand)


def check_left(grain:tuple, rocks:set, sand:list):
    if is_empty((grain[0]-1, grain[1]+1), rocks, sand):
        return grain
    
    return check_left((grain[0]-1, grain[1]+1), rocks, sand)
    

def check_right(grain:tuple, rocks:set, sand:list):
    if is_empty((grain[0]+1, grain[1]+1), rocks, sand):
        return grain

    return check_left((grain[0]+1, grain[1]+1), rocks, sand)

# I need a method that calls all the methods below to drop a piece of sand
# I need a method that checks down

def is_empty(position:tuple, rocks:set, sand:list):
    return position in rocks or position in sand


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