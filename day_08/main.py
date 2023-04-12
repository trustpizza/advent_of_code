def unique_values(old_list) -> list:
    new_list = []
    for item in old_list:
        if item not in new_list:
            new_list.append(item)
    return new_list
    
def get_visible_trees_from_reversed_list(trees) -> list:
    trees = (list(reversed(trees)))
    current_highest = -1
    visible_trees = []
    for tree_idx in range(len(trees)):
        if trees[tree_idx] > current_highest:
            visible_trees.append(tree_idx)
            current_highest = trees[tree_idx]

    visible_trees = list(map(lambda tree: abs(tree - 4), visible_trees))
    return visible_trees

def get_visible_trees_from_list(trees) -> list:
    current_highest = -1
    visible_trees = []
    for tree_idx in range(len(trees)):
        if trees[tree_idx] > current_highest:
            visible_trees.append(tree_idx) #technically the index of the tree
            current_highest = trees[tree_idx]
    return visible_trees

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
        highest_tree_idx_row = row.index(max(row))
        highest_tree_idx_col = col.index(max(col))

        # Split rows
        left_row_half = row[0:highest_tree_idx_row+1]
        right_row_half = row[highest_tree_idx_row:None]
        # Split Cols
        top_col_half = col[0:highest_tree_idx_col+1]
        bottom_col_half = col[highest_tree_idx_col:None]
        
        print(top_col_half, bottom_col_half)


        visible_left = get_visible_trees_from_list(left_row_half)
        visible_right = get_visible_trees_from_reversed_list(right_row_half)
        # print(left_row_half)
        for tree in visible_left:
            internal_tree_locations.append([row_idx,tree])
        for tree in visible_right:
            internal_tree_locations.append([row_idx, tree])

    # internal_tree_locations = unique_values(internal_tree_locations)
    return internal_tree_locations

def part_one(input_file):
    data = parse_input(input_file)
    visible_trees_count = 0
    # Step 1, get all perimeter values
    perimeter_trees = get_perimeter_trees(data)
    internal_trees = get_internal_trees(data)
    visible_trees =  unique_values(perimeter_trees+internal_trees)
    print(len(visible_trees))
    # visible_trees += len(perimeter_trees)
    return visible_trees_count


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