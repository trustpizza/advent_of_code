import os

def part_one(file_name: str) -> int:
    elf_calories = process_calories(file_name)
    return elf_calories

def part_two():
    return

def process_calories(file_name: str) -> list[list[int]]:
    with open(file_name, encoding="UTF-8") as f:
        elves = f.read().split("\n\n")
        print(elves)
    return

if __name__ == "__main__":
    file_dir = os.path.dirname(os.path.realpath("__file__"))
    input_file = "temp.txt" #temp is the small test file
    file_name = os.path.join(file_dir, input_file)
    print("---Part One---")
    print(part_one(file_name))