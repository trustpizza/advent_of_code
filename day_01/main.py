import os

def part_one(filename: str) -> int:
    elf_calories = process_calories(filename)
    return elf_calories

def part_two():
    return

def process_calories(filename: str) -> list[list[int]]:
    file = read_file(filename)
    #with open(filename, encoding="utf-8") as f:
        #elves = f.read().split("\n\n")
    return

def read_file(filename):
    file_handle = open(filename)
    print(file_handle.read())
    file_handle.close()

if __name__ == "__main__":
    file_dir = os.path.dirname(os.path.realpath("__file__"))
    input_file = "input.txt"
    file_name = os.path.join(file_dir, input_file)
    #print("/home/axel/advent_of_code/day_01/input.txt")
    #print("---Part One---")
    print(part_one(file_name))