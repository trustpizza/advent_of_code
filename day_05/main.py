import re

def part_one(input_file):
    print(parse_data(input_file))
    return

def part_two(input_file):
    return

def parse_data(input_file):
    # Take the input file
    # Read it
        # Take the read file
        # Split the data into two section
            # Wait for the first line that starts with "move", everything before that is the Data shape
            # Everything after that are the data moves

    # How to read the data
        # The last row, the one with columns has an identical number of spaces to an empty list.  
    data_shape = []
    moves = []
    with open(input_file) as f:
        file_lines = f.read().split("\n\n")
        for line in file_lines[0].splitlines():
            data_shape.append([*line])

        
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