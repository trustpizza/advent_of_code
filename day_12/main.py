class Hike:
    MOVES = [
        (0,1),
        (1,0),
        (-1,0),
        (0,-1)
    ]

    def __init__(self, heightmap, current_location, destination, prior_locations = []) -> object:
        self.current_value = 97
        self.current_location = current_location
        self.prior_locations = prior_locations
        self.heightmap = heightmap
        self.destination = destination

    def move(self):
        if self.check_hike_over():
            return self
        else:
            next_locations = []
            for move in Hike.MOVES:
                next_location = (self.current_location[0] + move[0], self.current_location[1] + move[1])
                next_location = self.check_next_location(next_location)
                next_locations.append(next_location)
            
            next_locations = [loc for loc in next_locations if loc is not None]

            for next_move in next_locations:
                prior_locations = list(self.prior_locations)
                prior_locations.append(next_move)
                
                next_hike = Hike(self.heightmap, next_move, self.destination, prior_locations)

                next_hike.move()
    
    def check_next_location(self, next_location):
        if (0 <= next_location[0] <= len(self.heightmap) -1) and (0 <= next_location[1] <= len(self.heightmap[0])-1) and (next_location not in self.prior_locations):
            
            return next_location
        else:
            return None

    def check_hike_over(self):
        return bool(self.current_location == self.destination) 

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
    best_path = shortest_route.move()
    return best_path

def parse_inputs(file):
    with open(file, encoding="utf8") as f:
        lines = f.read().splitlines()
    elevation_map = list(map(lambda line: list(map(lambda char: ord(char), line)),list([*line] for line in lines)))

    return elevation_map  

if __name__ == "__main__":
    filename = "temp.txt"
    print("---Part One---")
    print(part_one(filename))
