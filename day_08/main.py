def get_col_from_list(list) -> list:
    cols = []
    for row_idx in range(len(list)):
        col = []
        for col_idx in range(len(list[0])):
            col.append(list[col_idx][row_idx])
        cols.append(col)
    return cols
def get_perimeter_trees(forest) -> list:
    # Take the first row, the last row, the first col, and the last col
    perimeter_trees_locations = []
    # Get the location of each tree
    for idx, row in enumerate(forest):
        for col in range(len(row)):
            loc = [idx, col]
            if idx == 0 or idx == len(row)-1 or col == 0 or col == len(row) - 1:
                perimeter_trees_locations.append(loc)
    return perimeter_trees_locations

def get_internal_trees(forest) -> list:
    internal_tree_locations = []
    cols = get_col_from_list(forest)
    for row_idx, row in enumerate(forest):
        col = cols[row_idx]
        # First take rows, split each row in half by it's largest value
        for col_idx in range(len(row)):
            loc = [row_idx,col_idx]
            highest_tree_idx = row.index(max(row))
            # Rows First
            left_row_half = row[0:highest_tree_idx]
            right_row_half = row[highest_tree_idx:None]
            # Cols Second
            
            # print(left_row_half, right_row_half)

    return internal_tree_locations

def part_one(input_file):
    data = parse_input(input_file)
    visible_trees = 0
    # Step 1, get all perimeter values
    perimeter_trees = get_perimeter_trees(data)
    internal_trees = get_internal_trees(data)
    # print(internal_trees)
    # visible_trees += len(perimeter_trees)
    return visible_trees


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