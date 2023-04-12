def get_rows_from_cols(cols):
    rows = []
    for idx in range(len(cols[0])):
        row = []
        for col in cols:
            row.append(col[idx])
        rows.append(row)
    return rows

def part_one(input_file):
    data = parse_input(input_file)
    cols = data
    rows = get_rows_from_cols(cols)
    return 


def part_two(input_file):
    return

def parse_input(input_file):
    with open(input_file) as f:
        data = f.read().splitlines()
    return data

if __name__ == "__main__":
    input_file = "temp.txt"
    print("---Part One---")
    print(part_one(input_file))
    print("---Part Two---")
    print(part_two(input_file)) 