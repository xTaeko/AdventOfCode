import numpy as np

# Copied from https://stackoverflow.com/questions/1620940/determining-neighbours-of-cell-two-dimensional-list answer
neighbors = lambda x, y, xmax, ymax: [(x2, y2) for x2 in range(x - 1, x + 2)
                                  for y2 in range(y - 1, y + 2)
                                  if (-1 < x <= xmax-1 and
                                      -1 < y <= ymax-1 and
                                      (x != x2 or y != y2) and
                                      (0 <= x2 <= xmax-1) and
                                      (0 <= y2 <= ymax-1))]

def part_one():
    with open("Input.txt") as file:
        content = [list(map(int,list(row))) for row in file.read().splitlines()]
        array = np.array(content)
        xmax, ymax = array.shape
        flashes = 0

        for step in range(0,100):
            for x in range(0,xmax):
                for y in range(0,ymax):
                    array[x][y] += 1
                    # If it is 10, then it is flashing this moment. If it is higher than 10 it has flashed already.
                    if array[x][y] == 10:
                        add_energy_level_to_neighbors(array, neighbors(x,y, xmax, ymax))

            # Reset each Energy higher than 9
            for x in range(0,xmax):
                for y in range (0,ymax):
                    if array[x][y] > 9:
                        array[x][y] = 0
                        flashes +=1
        return flashes

# Use call-by-reference, therefore no return is needed
def add_energy_level_to_neighbors(array, list_coordinates):
    xmax, ymax = array.shape
    for x,y in list_coordinates:
        array[x][y] +=1
        if(array[x][y] == 10):
            add_energy_level_to_neighbors(array, neighbors(x,y,xmax,ymax))

result_part_one = part_one()
print("After 100 Steps, there were:", result_part_one, " flashes.")


# Copied almost everything from part one. But I want every Solution to be independent of each other.
def part_two():
    with open("Input.txt") as file:
        content = [list(map(int, list(row))) for row in file.read().splitlines()]
        array = np.array(content)
        xmax, ymax = array.shape
        # count steps, while condition is not met
        steps = 0
        while not np.all(array == 0):
            steps +=1
            for x in range(0, xmax):
                for y in range(0, ymax):
                    array[x][y] += 1
                    # If it is 10, then it is flashing this moment. If it is higher than 10 it has flashed already.
                    if array[x][y] == 10:
                        add_energy_level_to_neighbors(array, neighbors(x, y, xmax, ymax))

            # Reset each Energy higher than 9
            for x in range(0, xmax):
                for y in range(0, ymax):
                    if array[x][y] > 9:
                        array[x][y] = 0
        return steps


result_part_two = part_two()
print(result_part_two, "is the first step where all octopuses flashes at the same time.")