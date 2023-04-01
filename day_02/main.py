import os

def part_one(file_name):
    with open(file_name) as file:
        x = file.read()
        print(x)
    return

def part_two():
    return

if __name__ == "__main__":
    file_dir = os.path.dirname(os.path.realpath("__file__"))
    input_file = "temp.txt" #temp is the small test file
    file_name = os.path.join(file_dir, input_file)

    print("---Part One---")
    print(part_one(file_name))
    #print("---Part Two---")
    #print(part_two(file_name))