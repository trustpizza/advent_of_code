# 
# Day 3
#

# 
import os

def search_rucksack(left_half, right_half, lpointer=0):
    target = left_half[lpointer]
    # What are my break points for this recursion
    # 
    for idx, item in enumerate(right_half):
        if target == item:
            return item
    lpointer +=1

    search_rucksack(left_half, right_half, lpointer)
    
    return

def split_and_search_rucksack(rucksack):
    left_half = rucksack[:int(len(rucksack)/2)]
    right_half = rucksack[int(len(rucksack)/2):]

    search_rucksack(left_half, right_half)

    return
    
def part_one(file_name):
    rucksacks = process_rucksacks(file_name)
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
    return split_and_search_rucksack(rucksacks[0])

def part_two(file_name):
    return

def process_rucksacks(file_name):
    with open(file_name) as f:
        rucksacks = f.read().split()
    return [list(map(list,rucksack)) for rucksack in rucksacks]

if __name__ == "__main__":
    file_dir = os.path.dirname(os.path.realpath("__file__"))
    input_file = "temp.txt" #temp is the small test file
    file_name = os.path.join(file_dir, input_file)

    print("---Part One---")
    print(part_one(file_name))
    print("---Part Two---")
print(part_two(file_name))