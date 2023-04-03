# 
# Day 3
#

# 
import os

def part_one(file_name):
    # take rucksacks
    # Take each rucksack
    # Split it into a left and right half
        # Left Container: pointer on left[pointer]
            # pointer2 value is equal to 0
            #Check right[pointer2] for item
            # If left[pointer] == right[pointer2]
                # return left[pointer]
            # If left[pointer] != right[pointer2]
                # pointer2++
            # if left[pointer != right[pointer2] AND pointer2 is the last item in the list
                # Restart at pointer++
    return process_rucksacks(file_name)

def part_two(file_name):
    return

def process_rucksacks(file_name):
    with open(file_name) as f:
        rucksacks = f.read().split()
    return rucksacks

if __name__ == "__main__":
    file_dir = os.path.dirname(os.path.realpath("__file__"))
    input_file = "temp.txt" #temp is the small test file
    file_name = os.path.join(file_dir, input_file)

    print("---Part One---")
    print(part_one(file_name))
    print("---Part Two---")
print(part_two(file_name))