def part_one(input_file):
    first_four_non_repeating = test_string(parse_input(input_file))
    return first_four_non_repeating

def part_two(input_file):
    string = parse_input(input_file)
    string_as_list = [*string]
    for idx, char in enumerate(string_as_list):
        if idx > 13:
            if len(string_as_list[idx-14:idx]) == len(set(string_as_list[idx-4:idx])): return idx
    return

def parse_input(input_file):
    with open(input_file) as f:
        data = f.read()
    return data

def test_string(string):
    string_as_list = [*string]
    for idx, char in enumerate(string_as_list):
        if idx > 3:
            if len(string_as_list[idx-4:idx]) == len(set(string_as_list[idx-4:idx])): return idx


if __name__ == "__main__":
    input_file = "input.txt" #temp is the small test file
    print("---Part One---")
    print(part_one(input_file))
    print("---Part Two---")
    print(part_two(input_file))
    # print("---Test---")
    # print(test_string("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))