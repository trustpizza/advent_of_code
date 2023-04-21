import math

class Monkey:

    instances = []
    worry_level = 0

    def __init__(self, id, starting_items, operation, test, truth_condition_id, false_condition_id) -> None:
        self.id = id
        self.starting_items = starting_items
        self.__operation = operation
        self.__test = test
        self.truth_condition_id = truth_condition_id
        self.false_condition_id = false_condition_id
        self.items_inspected = 0
        
        Monkey.instances.append(self)

    def take_turn(self):
        for item in self.starting_items[:]:
            Monkey.worry_level = self.operate(item)
            Monkey.worry_level = math.floor(Monkey.worry_level / 3)
            print(Monkey.worry_level)
            self.throw_item(item)


    def operate(self, item):
        return self.__operation(item)
        
    def test_worry(self, item):
        print(item, self.__test(item))
        return self.__test(item)

    def throw_item(self, item):
        self.starting_items.remove(item)

        if self.test_worry(Monkey.worry_level):
            Monkey.find(self.truth_condition_id).catch(item)
        else:
            Monkey.find(self.false_condition_id).catch(item)
    
    def catch(self, item: int):
        self.starting_items.append(item)

    @classmethod
    def find(cls, id):
        return [monkey for monkey in cls.instances if monkey.id == id][0]
        

def test(file):
    parse_inputs(file)
    monkey = Monkey.find(0)
    m2 = Monkey.find(2)
    m3 = Monkey.find(3)

    print(monkey.starting_items)
    print(m2.starting_items, m3.starting_items)

    monkey.take_turn()
    print(monkey.starting_items)
    print(m2.starting_items, m3.starting_items)        

def part_one(file):
    # parse_inputs(file)

    # for monkey in Monkey.instances:
    #     for item in monkey.starting_items:
    #         # Take the item
    #         # 
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

def get_test(test):
    num = int(test.split(" ")[-1])
    return lambda x: bool(x % num == 0)

def parse_inputs(file):
    with open(file, encoding="utf-8") as f:
        for monkey in f.read().split("\n\n"):
            monkey = monkey.split("\n")

            id = int(monkey[0].split(" ")[1].replace(":", ""))
            starting_items = [int(num) for num in monkey[1].split(": ")[1].split(", ")]
            operation = get_operation(monkey[2])
            test = get_test(monkey[3])
            truth_condition_id = int(monkey[4].split(" ")[-1])
            false_condition_id = int(monkey[5].split(" ")[-1])

            monkey = Monkey(id, starting_items, operation, test, truth_condition_id, false_condition_id)

if __name__ == "__main__":
    input_path = "temp.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))

    print("---Test----")
    print(test(input_path))