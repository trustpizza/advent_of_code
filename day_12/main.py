class Hike:
    MOVES = [
        (0,1),
        (1,0),
        (-1,0),
        (0,-1)
    ]

    possible_outcomes = []

    def __init__(self, heightmap, current_location, destination, prior_locations = []) -> object:
        self.current_location = current_location
        self.prior_locations = prior_locations
        self.heightmap = heightmap
        self.destination = destination
        self.current_value = self.find_current_value()


    def find_current_value(self):
        return self.heightmap[self.current_location[0]][self.current_location[1]]

    def move(self):
        self.check_hike_over()

        next_locations = []
        for move in Hike.MOVES:
            next_location = (self.current_location[0] + move[0], self.current_location[1] + move[1])
            next_location = self.check_next_location(next_location)
            if next_location is not None: next_locations.append(next_location)
        
        next_locations = list(map(lambda x: is_legal_move(self.current_value, x, self.heightmap), next_locations))
        next_locations = list(filter(lambda x: x is not None, next_locations))

        for next_move in next_locations:
            prior_locations = list(self.prior_locations)
            prior_locations.append(next_move)

            next_hike = Hike(self.heightmap, next_move, self.destination, prior_locations)

            next_hike.move()
    
    def check_next_location(self, next_location):
        if (0 <= next_location[0] <= len(self.heightmap) -1) and (0 <= next_location[1] <= len(self.heightmap[0])-1) and (next_location not in self.prior_locations):
            return next_location
        else:
            return 

    def check_hike_over(self):
        if self.current_location == self.destination:
            Hike.possible_outcomes.append(self)

def is_legal_move(current_value, move, heightmap):
    if heightmap[move[0]][move[1]] in range(current_value - 1, current_value+2):
        return move

def part_one(file):
    heightmap = parse_inputs(file)
    for i, line in enumerate(heightmap):
        for j,char in enumerate(line):
            if char == 83:
                start = (i,j)
                heightmap[i][j] = 97
            if char == 69:
                destination = (i,j)
                heightmap[i][j] = 122

    shortest_route = Hike(heightmap, start, destination)
    shortest_route.move()

    lens_outcomes = []

    for route in Hike.possible_outcomes:
        lens_outcomes.append(len(route.prior_locations))

    return min(lens_outcomes)

def parse_inputs(file):
    with open(file, encoding="utf8") as f:
        lines = f.read().splitlines()
    elevation_map = list(map(lambda line: list(map(lambda char: ord(char), line)),list([*line] for line in lines)))

    return elevation_map  

if __name__ == "__main__":
    filename = "input.txt"
    print("---Part One---")
    print(part_one(filename))
