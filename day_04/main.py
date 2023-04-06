import re

def get_diff(pair):
    return pair[1] - pair[0]

def part_one(file_path):
    counter = 0
    assignments = parse_data(file_path)
    for pair in assignments:
        larger_pair = pair[0] if get_diff(pair[0]) > get_diff(pair[1]) else pair[1] # if diff pair[0][1] - pair[0][0] > pair[1][1] - pair[]
        smaller_pair = pair[0] if get_diff(pair[0]) <= get_diff(pair[1]) else pair[1]

        range_of_smaller = list(range(smaller_pair[0], smaller_pair[1] + 1))
        
        check = all(larger_pair[0] <= item <= larger_pair[1] for item in range_of_smaller)

        if check: counter += 1
    return counter

def part_two(file_path):
    counter = 0
    assignments = parse_data(file_path)
    for pair in assignments:
        larger_pair = pair[0] if get_diff(pair[0]) > get_diff(pair[1]) else pair[1] # if diff pair[0][1] - pair[0][0] > pair[1][1] - pair[]
        smaller_pair = pair[0] if get_diff(pair[0]) <= get_diff(pair[1]) else pair[1]

        range_of_smaller = list(range(smaller_pair[0], smaller_pair[1] + 1))
        
        check = any(larger_pair[0] <= item <= larger_pair[1] for item in range_of_smaller)

        if check: counter += 1
    return counter

    return

def parse_data(file_path):
    assignments = []
    with open(file_path) as f:
        lines = f.read().strip().split()
        for line in lines:
            a,b,c,d = map(int, re.findall(r"\d+", line))
            assignments.append([[a,b],[c,d]])

    # assignments = []
    # with open(file_path, encoding="utf-8") as f:
    #     lines = f.read().strip().split("\n")
    #     for line in lines:
    #         a, b, c, d = map(int, re.findall(r"\d+", line))
    #         assignments.append([(a, b), (c, d)])
    # return assignments
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
    input_file = "input.txt" #temp is the small test file
    print("---Part One---")
    print(part_one(input_file))
    print("---Part Two---")
    print(part_two(input_file)) 