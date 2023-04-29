from functools import reduce
from operator import concat

def part_one(file):
    rocks = parse_inputs(file)
    y_max = max([y for _, y in rocks]) # Max Depth
    sand_heap = set()
    abyss = False

    while not abyss:
        new_sand = (500,0)
        current_position = new_sand
        rest = False
        while not rest:
            if current_position[1] > y_max:
                abyss = True
                break
            for dx, dy in [(0,1), (-1,1), (1,1)]: # Down, Left, Right
                next_position = (current_position[0]+dx, current_position[1]+dy)
                if next_position not in rocks | sand_heap:
                    current_position = next_position
                    break
            else:
                rest = True
                sand_heap.add(current_position)
    return len(sand_heap)


def part_two(file):
    rocks = parse_inputs(file)
    y_max = max([y for _,y in rocks])
    sand_heap = {(500,0)}
    queue = {(500,0)}

    while queue:
        current_position = queue.pop()
        if current_position[1] >= y_max +1:
            continue
        for dx, dy in [(0,1), (-1,1), (1,1)]:
            next_position = (current_position[0]+dx, current_position[1]+dy)
            if next_position not in rocks:
                sand_heap.add(next_position)
                queue.add(next_position)

    return len(sand_heap)

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
    
    rocks = []
    
    for line in lines:
        for idx in range(len(line)):
            if idx < len(line) - 1:
                rock_row = find_rocks(line[idx], line[idx+1])
                rocks.append(rock_row)
    rocks = set(list(reduce(concat, rocks)))
    return rocks


if __name__ == "__main__":
    filename = 'input.txt'
    print("---Part One---")
    print(part_one(filename))
    print("---Part Two---")
    print(part_two(filename))