def part_one(file):
    input = parse_inputs(file)
    return input

def parse_inputs(file):
    with open(file, encoding="utf8") as f:
        lines = f.read().splitlines()
    elevation_map = list(map(lambda line: list(map(lambda char: ord(char), line)),list([*line] for line in lines)))

    return elevation_map  

if __name__ == "__main__":
    filename = "temp.txt"
    print("---Part One---")
    print(part_one(filename))
