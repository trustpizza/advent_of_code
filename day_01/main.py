import os

def part_one(file_name: str) -> int:
    elf_calories = process_calories(file_name)
    max = 0
    for elf in elf_calories:
        if max <= sum(elf):
            max = sum(elf)
    return max

def part_two(file_name: str) -> int:
    elf_calories = process_calories(file_name)
    sum_of_all = [sum(elf) for elf in elf_calories]

    top_3_calories = sorted(sum_of_all, reverse=True)[0:3]
    return sum(top_3_calories)

def process_calories(file_name: str) -> list[list[int]]:
    with open(file_name, encoding="UTF-8") as f:
        elves = f.read().split("\n\n")
    return [list(map(int, elf.strip().split('\n'))) for elf in elves]

if __name__ == "__main__":
    file_dir = os.path.dirname(os.path.realpath("__file__"))
    input_file = "input.txt" #temp is the small test file
    file_name = os.path.join(file_dir, input_file)

    print("---Part One---")
    print(part_one(file_name))
    print("---Part Two---")
    print(part_two(file_name))