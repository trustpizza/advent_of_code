class File:
    def __init__(self, file_string):
        self.name = find_file_name(file_string)
        self.size = find_file_size(file_string)

def find_file_name(string):
    return string.split(" ")[1]

def find_file_size(string):
    return string.split(" ")[0]

def part_one(input_file):
    # Split lines
    # Every time you find a command, list out the consecutive lines from there and group those as "response"
    print(group_commands(input_file))
    f1 = File("14848514 b.txt")
    return f1.size

def part_two(input_file):
    return

def group_commands(input_file):
    with open(input_file) as f:
        f.read().splitlines()
    return f

if __name__ == "__main__":
    input_file = "temp.txt"
    print("---Part One---")
    print(part_one(input_file))
    print("---Part Two---")
    print(part_two(input_file)) 