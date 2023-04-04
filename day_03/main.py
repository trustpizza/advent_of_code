# 
# Day 3
#

# 
import os

def find_priority(char):
    val = 0
    if ord(char) <= 90:
        val = ord(char)-65 + 27
    else: 
        val = ord(char) - 96
    return val

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
    return

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