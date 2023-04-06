

def part_one(file_path):
    # Set a counter to 0
    # Take the file input and split it one each line
        # Take ech line and split it on the comma > this is your 2 elf pair 
            # Each elf can be represented as an array of length elf[1] - elf[0]
            # Take that elf and add every number between (and including) elf[0] and elf[1] to create an array of elf[1] - elf[0] length
            # Do this for both elves
        # Take the smaller elf (the larger elf can NEVER be fully contained by the other elf)
            # Test to see if all of it's values exist in the larger elf
                # If true, coutner ++ 
                # Else, next elf pair
    # Return counter
    return

def part_two(file_path):
    return

def open_file(file_path):
    with open(file_path) as f:
        x = f.read()
    print(x)

if __name__ == "__main__":
    file_dir = "./"
    #file_dir = os.path.dirname(os.path.realpath("__file__"))
    input_file = "temp.txt" #temp is the small test file
    file_name = os.path.join(file_dir, input_file)
    print("---Part One---")
    print(part_one(input_file))
    print("---Part Two---")
    print(part_two(file_name))