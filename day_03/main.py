# 
# Day 3
#

# 
import os
import itertools as it
import more_itertools as mit

def find_priority(char):
    val = 0
    if ord(char) <= 90:
        val = ord(char)-65 + 27
    else: 
        val = ord(char) - 96
    return val

def search_group(group):
    elves = []
    for elf in group:
        flattened_elf = (list(it.chain(*elf)))
        elves.append(flattened_elf)
    
    shared_char = None
    
    for idx, char in enumerate(elves[0]):
        if char in elves[1] and char in elves[2]:
            shared_char = char

    return shared_char

def split_and_search_rucksack(rucksack):
    left_half = rucksack[:int(len(rucksack)/2)]
    right_half = rucksack[int(len(rucksack)/2):]

    for val, char in enumerate(rucksack):
        if char in right_half and char in left_half:
            return char


    return char

def part_one(file_name):
    rucksacks = process_rucksacks(file_name)
    priorities = []

    for rucksack in rucksacks:
        shared_letter = split_and_search_rucksack(rucksack)[0]
        priority = find_priority(shared_letter)
        priorities.append(priority)

    

    return sum(priorities)

def part_two(file_name):
    rucksacks = process_rucksacks(file_name)
    three_elf_group = list(mit.chunked(rucksacks, 3))

    shared = []
    for group in three_elf_group:
        shared_letter = search_group(group)
        shared.append(shared_letter)
    # for group in three_elf_group:
    #     shared_letter = search_group(group)
    #     print(shared_letter)
    priorities = []
    for char in shared:
        priority = find_priority(char)
        priorities.append(priority)
    
    return sum(priorities)   

def process_rucksacks(file_name):
    with open(file_name) as f:
        rucksacks = f.read().split()
    return [list(map(list,rucksack)) for rucksack in rucksacks]

if __name__ == "__main__":
    file_dir = os.path.dirname(os.path.realpath("__file__"))
    input_file = "input.txt" #temp is the small test file
    file_name = os.path.join(file_dir, input_file)

    print("---Part One---")
    print(part_one(file_name))
    print("---Part Two---")
print(part_two(file_name))