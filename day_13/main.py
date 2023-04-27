import ast
from functools import cmp_to_key

def part_one(file):
    line_pairs = parse_inputs(file)
    return sum([idx for idx, pair in enumerate(line_pairs, 1) if compare(*pair) == 1])# if compare(*pair)])

def part_two(file):
    line_pairs = parse_inputs(file)
    keys = [[[2]],[[6]]]
    # flattened_lines = [item for subline in line_pairs for item in subline]
    flattened_lines = keys + [item for sublist in line_pairs for item in sublist]
    flattened_lines.sort(key=cmp_to_key(compare), reverse=True)
    print(flattened_lines)

# Return -1 if not ordered, 0 if equal, 1 if ordered
def compare(left: list | int, right: list | int):
    match left, right:
        case int(), int():
            return (left < right) - (left > right)
        case list(), list():
            for compare_val in map(compare, left, right):
                if compare_val:
                    return compare_val
            return compare(len(left), len(right))

        case int(), list():
            return compare([left], right)
        case list(), int():
            return compare(left, [right])


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
    print("---Part Two---")
    print(part_two(filename))