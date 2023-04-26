import ast

def part_one(file):
    line_pairs = parse_inputs(file)
    return 

def parse_inputs(file):
    with open(file, encoding="utf8") as f:
        return [
            [ast.literal_eval(line) for line in pair.strip().split("\n")]
            for pair in f.read().split("\n\n")
        ]
        

if __name__ == "__main__":
    filename = "temp.txt"
    print("---Part One---")
    print(part_one(filename))