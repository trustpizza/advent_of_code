class Directory:
    def __init__(self) -> None:
        pass

class File:
    def __init__(self, file_string):
        self.name = file_string.split(" ")[1]
        self.size = file_string.split(" ")[0]


def part_one(input_file):
    # Split lines
    # Every time you find a command, list out the consecutive lines from there and group those as "response"
    print(group_commands(input_file))
    f1 = File("14848514 b.txt")
    return 

def part_two(input_file):
    return

def group_commands(input_file):
    with open(input_file) as f:
        terminal_data = f.read().strip().split("\n")

    groups = []
    group = []
    for command in terminal_data:
        if command.startswith("$ cd"):
            # Start a new group
            if group:
                groups.append(group)
            group = [command]
        else:
            # Add command to current group
            group.append(command)

    # Add the final group
    if group:
        groups.append(group)

    return groups

    

if __name__ == "__main__":
    input_file = "temp.txt"
    print("---Part One---")
    print(part_one(input_file))
    print("---Part Two---")
    print(part_two(input_file)) 