import re

def find_dirs(ls):
    dirs = []
    for obj in ls:
        if is_dir(obj): dirs.append(obj)
    return dirs

def find_files(ls):
    files = []
    for obj in ls: 
        if is_file(obj): files.append(obj)
    return files

def is_file(string):
    pattern1 = r"\d*\s\w+$"
    pattern2 = r".[A-Za-z]{3}$"
    # return bool(re.match(pattern2, string[-4:]))
    first_case = bool(re.match(pattern1, string))
    return bool(re.match(pattern1, string) or re.match(pattern2, string[-4:]))

def is_dir(string):
    return string.startswith("dir")
    # return bool(string.startswith("dir"))

def parse_group(group):
    pass

class Directory:
    def __init__(self,parent = None) -> None:
        self.files = []
        self.child_dirs = []
        self.parent = parent
        pass

    def add_dir(dir) -> None:
        pass

    def add_file(self,file) -> None:
        self.files.append(file)
    
    def print_input(self):
        print(self.files)

class File:
    def __init__(self, file_string):
        self.name = file_string.split(" ")[1]
        self.size = file_string.split(" ")[0]


def part_one(input_file):
    command_blocks = group_commands(input_file)
    for block in command_blocks:
        print(block)

    test = command_blocks[0]
    root = Directory()
    current_dir = None
    #Create a root directory
    # Find all files within it, add those files
    # Find all subdirectories, add those directories
    
    # child_dirs = find_dirs(test)
    # files = find_files(test)

    # for dir in child_dirs:
    #     dir_command = "$ cd " + dir.split(" ")[1]
    #     for command_block in command_blocks:
    #         if command_block[0] == dir_command:
    #             print(command_block)

    # print(child_dirs, files)

    # for command_block in command_blocks:
    #     if command_block[0].endswith("/"): 
    #         current_dir = root
    #     else:
    #         current_dir = Directory(command_block[0].split()[2])
    #     for command in command_block:
    #         # print(is_file(command),command)
    #         if is_file(command):
    #             current_dir.add_file(command)
    #         elif is_dir(command):
    #             print(command)
    #             # dir.add_dir(command)


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