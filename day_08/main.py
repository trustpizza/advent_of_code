
def part_one(input_file):
    data = parse_input(input_file)

    return data


def part_two(input_file):
    return

def parse_input(input_file):
    with open(input_file) as f:
        rows = []
        data = f.read().splitlines()
        for row in data:
            row = list(map(int, [*row]))
            rows.append(row)
    return rows

if __name__ == "__main__":
    input_file = "temp.txt"
    print("---Part One---")
    print(part_one(input_file))
    print("---Part Two---")
    print(part_two(input_file)) 