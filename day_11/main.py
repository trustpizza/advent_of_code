class Monkey:

    instances = []

    def __init__(self, id, starting_items, operation, test, true_target, false_target) -> None:
        self.id = id
        self.starting_items = starting_items
        self.operation = operation
        self.test = test

        Monkey.instances.append(self)
    
    def inspect_item(self):
        item = self.starting_items[0]
    
    @classmethod
    def find(cls, id):
        return [monkey for monkey in cls.instances if monkey.id == id]
        

def test():
    id = 0
    starting_items = [79, 98]
    operation = lambda old: old * 19
    test = lambda x: x % 3 == 0
    true_target = 2
    false_target = 3

    m1 = Monkey(id, starting_items, operation, test, true_target, false_target)
    m2 = Monkey.find(1)
    print(m1,m2)

def part_one(file):
    pass

def part_two(file):
    pass

if __name__ == "__main__":
    input_path = "input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))

    print("---Test----")
    print(test())