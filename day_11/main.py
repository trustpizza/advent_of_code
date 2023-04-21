class Monkey:

    instances = []

    def __init__(self, id, starting_items, operation, test, true_target, false_target) -> None:
        self.id = id
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.true_target = true_target
        self.false_target = false_target
        
        Monkey.instances.append(self)

    def __operate(self, item):
        return self.operation(item)
        
    def test_item(self, item):
        return self.test(item)
    
    def inspect_item(self,item):
        item = self.__operate(item)
        if self.test_item(item):
            return Monkey.find(self.true_target)
        else:
            return Monkey.find(self.false_target)

    @classmethod
    def find(cls, id):
        return [monkey for monkey in cls.instances if monkey.id == id]
        

def test():
    id = 0
    starting_items = [79, 98]
    operation = lambda old: old * 19
    test = lambda x: bool(x % 3 == 0)
    true_target = 2
    false_target = 3

    m1 = Monkey(id, starting_items, operation, test, true_target, false_target)
    print(m1.inspect_item(m1.starting_items[1]))

def part_one(file):
    parse_inputs(file)
    pass

def part_two(file):
    pass

def get_operation(operation):
    func = operation.split("= ")[1]
    operator = func.split(" ")[1]
    addend_or_multiplicand = func.split(operator)[-1]

    out = None

    if operator == "+":
        if addend_or_multiplicand == " old":
            out = lambda x: x + x
        else:
            out = lambda x: x + int(addend_or_multiplicand)
    elif operator == "*":
        if addend_or_multiplicand == " old":
            out = lambda x: x * x

        else:
            out = lambda x: x * int(addend_or_multiplicand)

    return out

def parse_inputs(file):
    with open(file, encoding="utf-8") as f:
        for monkey in f.read().split("\n\n"):
            # monkey = monkey.split("\n")
            monkey = monkey.split("\n")
            id = int(monkey[0].split(" ")[1].replace(":", ""))
            starting_items = [int(num) for num in monkey[1].split(": ")[1].split(", ")]
            operation = get_operation(monkey[2])

            print(operation(2))
            # print(monkey)
            print("next monkeY")
    # print(monkeys)


if __name__ == "__main__":
    input_path = "temp.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))

    print("---Test----")
    print(test())