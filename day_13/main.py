def part_one(file):
    line_pairs = parse_inputs(file)
    return 

def parse_inputs(file):
    with open(file, encoding="utf8") as f:
        line_pairs = f.read().split("\n\n")
        line_pairs = list(map(lambda pair: pair.split("\n"), line_pairs))
    return line_pairs

if __name__ == "__main__":
    filename = "temp.txt"
    print("---Part One---")
    print(part_one(filename))