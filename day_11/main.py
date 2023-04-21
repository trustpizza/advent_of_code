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
            self.items_inspected += 1
            Monkey.worry_level = self.operate(item)
            Monkey.worry_level = math.floor(Monkey.worry_level)
            self.throw_item(item)

    def operate(self, item):
        return self.__operation(item)
        
    def test_worry(self, item):
        return self.__test(item)

    def throw_item(self, item):
        self.starting_items.remove(item)

        if self.test_worry(Monkey.worry_level):
            Monkey.find(self.truth_condition_id).catch(int(Monkey.worry_level))
        else:
            Monkey.find(self.false_condition_id).catch(int(Monkey.worry_level))
    
    def catch(self, item: int):
        self.starting_items.append(item)

    @classmethod
    def find(cls, id):
        return [monkey for monkey in cls.instances if monkey.id == id][0]
        
def Nmaxelements(list1, N):
    final_list = []
 
    for i in range(0, N):
        max1 = 0
 
        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j]
 
        list1.remove(max1)
        final_list.append(max1)  
    return final_list

def test(file):  
    pass

def part_one(file):
    return
    parse_inputs(file)

    for i in range(20):
        for monkey in Monkey.instances:
            monkey.take_turn()            
            
    final = []
    for monkey in Monkey.instances:
        final.append(monkey.items_inspected)

    largest_2 = Nmaxelements(final, 2)

    monkey_business = largest_2[0] * largest_2[1]

    return monkey_business


def part_two(file):
    parse_inputs(file)
    
    for i in range(1000):
        for monkey in Monkey.instances:
            monkey.take_turn()            
            
    final = []
    for monkey in Monkey.instances:
        print(monkey.items_inspected)
        final.append(monkey.items_inspected)

    largest_2 = Nmaxelements(final, 2)

    monkey_business = largest_2[0] * largest_2[1]
    print(final)
    return monkey_business

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