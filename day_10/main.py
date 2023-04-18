def part_one(file):
    cycles = process_input(file)

    val = 0

    for v in [20,60,100,140,180,220]:
        val += (v*cycles[v])

    return val

def part_two(file):
    cycles = process_input(file)
    # drawn = []
    # for position in range(240):
    #     cycle = position +1
    #     val = get_val(cycles, cycle)
    #     target = position % 40 - val
    #     if -1 <= target <= 1: 
    #         drawn.append(position)

    cycles = process_input(file)
    drawn = []
    for position in range(240):
        cycle = position + 1
        register_val = get_val(cycles, cycle)
        target = position % 40 - register_val
        if -1 <= target <= 1:
            drawn.append(position)
    show_screen(drawn)



def get_val(cycles, cycle):
    if cycle in cycles:
        return cycles[cycle]
    elif cycle-1 in cycles:
        return cycles[cycle-1]
    elif cycle-2 in cycles:
        return cycles[cycle-2]

def show_screen(drawn: list[int]) -> None:
    for y in range(6):
        for x in range(40):
            if x + y * 40 in drawn:
                print("#", end="")
            else:
                print(".", end="")
        print()

def process_input(filename: str) -> dict[int,int]:
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
    input_path = "input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))