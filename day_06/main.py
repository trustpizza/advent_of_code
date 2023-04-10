def part_one(input_file):
    print(parse_input(input_file))
    return

def part_two(input_file):
    return

def parse_input(input_file):
    with open(input_file) as f:
        f.read().split("\n")
    return f

if __name__ == "__main__":
    input_file = "input.txt" #temp is the small test file
    print("---Part One---")
    print(part_one(input_file))
    print("---Part Two---")
    print(part_two(input_file)) 