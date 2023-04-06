

def part_one(file_path):
    open_file(file_path)
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