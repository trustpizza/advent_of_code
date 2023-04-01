import os

def part_one(file_name):
    print(process_rps(file_name))
    return

def part_two():
    return

def process_rps(file_name):
    with open(file_name) as f:
        combos = f.read()
    combos = combos.split()
    "".join(combos)

    return ["".join(x) for x in zip(combos[0::2], combos[1::2])]

if __name__ == "__main__":
    file_dir = os.path.dirname(os.path.realpath("__file__"))
    input_file = "temp.txt" #temp is the small test file
    file_name = os.path.join(file_dir, input_file)

    print("---Part One---")
    print(part_one(file_name))
    #print("---Part Two---")
    #print(part_two(file_name))