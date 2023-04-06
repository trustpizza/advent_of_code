import re

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
    counter = 0
    print(open_file(file_path))
    return

def part_two(file_path):
    return

def open_file(file_path):
    assignments = []
    with open(file_path) as f:
        lines = f.read().strip().split()
        for line in lines:
            a,b,c,d = map(int, re.findall(r"\d", line))
            assignments.append([[a,b],[c,d]])

        # lines = f.read().strip().split()
        # for temp_line in lines:
        #     temp_line = temp_line.split(",")
        #     temp_line = [list(val) for val in temp_line]
        #     line = []
        #     for elf in temp_line:
        #         elf.remove("-")
        #         elf = [eval(num) for num in elf]
        #         line.append(elf)
        #     assignments.append(line)
    # THis is an ugly way to do this, but I can't find a better since whenever I map the elves, it resets it to a string
    return assignments

if __name__ == "__main__":
    input_file = "temp.txt" #temp is the small test file
    print("---Part One---")
    print(part_one(input_file))
    print("---Part Two---")
    print(part_two(input_file)) 