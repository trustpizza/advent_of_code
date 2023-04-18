def part_one(file):
    cycles = proces_input(file)
    return 

def part_two(file):
    pass

def proces_input(filename: str) -> dict[int,int]:
    cycle_count = 1
    x = 1
    cycle_values = {cycle_count: x}

    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]
   
    for line in lines:
        match line.split():
            case ["noop"]:
                cycle_count += 1
                cycle_values[cycle_count] = x
            case ["addx", v]:
                cycle_count += 1
                cycle_values[cycle_count] = x
                cycle_count += 1
                x += int(v)
                cycle_values[cycle_count] = x
    return cycle_values 

if __name__ == "__main__":
    input_path = "temp.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))