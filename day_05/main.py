def part_one(input_file):
    input_data = parse_data(input_file)
    container_group = input_data[0]
    moves = input_data[1]

    for move in moves:
        how_many = move[0]
        start = move[1] - 1
        destination = move[2] - 1

        containers_moved = container_group[start][0:how_many]
        for container in containers_moved:
            container_group[destination].insert(0,container)
            # container_group[destination].append(container)
            #print("Moving:" + container_group[start][0:how_many] + "From:" + container_group[start] + "To:" + container_group[destination] + "Currently:" + container_group + "")
        del container_group[start][0:how_many]

    first_of_each_container_group = []

    for stack in container_group:
        first_of_each_container_group.append(stack[0])
        # print(group[0])
    return first_of_each_container_group

def part_two(input_file):
    return

def get_data_shape(container_data):
    data_shape = []
    col_nums = container_data[-1]
    for i, num in enumerate(col_nums):
        if num != " ":    
            col = []
            for line in container_data[:-1]:
                if line[i] != " ": 
                    col.append(line[i]) 
            data_shape.append(col)
    return data_shape

def clean_move(move):
    cleaned_move = []
    move = move.split()
    cleaned_move.append(int(move[1]))
    cleaned_move.append(int(move[3]))
    cleaned_move.append(int(move[5]))

    return cleaned_move

def get_moves(move_lines):
    moves = []
    for move in move_lines:
        moves.append(clean_move(move))
    return moves

def parse_data(input_file):
    # Take the input file
    # Read it
        # Take the read file
        # Split the data into two section
            # Wait for the first line that starts with "move", everything before that is the Data shape
            # Everything after that are the data moves

    # How to read the data
        # The last row, the one with columns has an identical number of spaces to an empty list.  
    # Data shape is the 
    with open(input_file) as f:
        file_lines = f.read().split("\n\n")
        data_lines = []
        move_lines = []
        for line in file_lines[0].splitlines():
            data_lines.append([*line])
        for line in file_lines[1].splitlines():
            move_lines.append(line)

    data_shape = get_data_shape(data_lines)
    moves = get_moves(move_lines)
    
    return [data_shape, moves]

def test(input_file):
    with open(input_file) as f:
        file_lines = f.read().split("\n\n")
        print(file_lines)

if __name__ == "__main__":
    input_file = "temp.txt" #temp is the small test file
    print("---Part One---")
    print(part_one(input_file))
    #test(input_file)
    print("---Part Two---")
    print(part_two(input_file)) 