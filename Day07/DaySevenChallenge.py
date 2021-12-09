import math

import numpy as np


def part_one():
    # Maximal Input 1991
    with open("Input.txt") as file:
        input = file.read().splitlines()
        # Create List of splittet values, afterwards use list comprehension for using int function over all of them. Unpack list afterwards
        content = [[int(item) for item in line.split(",")] for line in input][0]

        # Create Dummy array with infinite values, to not provide the minimum automatically
        fuel_costs = np.full(max(content), math.inf)

        for position in range(0, max(content)):
            tmp = [abs(ship_position - position) for ship_position in content]
            fuel_costs[position] = np.sum(tmp)
        fuel_costs[0] = math.inf

        return min(fuel_costs)


result_part_one = part_one()
print("The minimum fuel usage is: ", result_part_one)


def part_two():
    with open("Input.txt") as file:
        input = file.read().splitlines()
        # Create List of splittet values, afterwards use list comprehension for using int function over all of them. Unpack list afterwards
        content = [[int(item) for item in line.split(",")] for line in input][0]
        maximum_position = max(content)
        fuel_costs = np.full(maximum_position, math.inf)
        list_fuel = calculate_fuel_list(2000)

        for wanted_position in range(0, maximum_position):
            tmp = [list_fuel[abs(ship_position - wanted_position)] for ship_position in content]
            fuel_costs[wanted_position] = np.sum(tmp)
        # Delete Position 0 because it does not exists.
        fuel_costs[0] = math.inf
        return min(fuel_costs)


# Precalculate the fuel for all distances to use later
def calculate_fuel_list(end_position) -> list:
    distance = abs(0 - end_position)
    fuel_list = [0]
    fuel = 0
    for index in range(1, distance + 1):
        fuel += index
        fuel_list.append(fuel)

    return fuel_list


result_part_two = part_two()
print("The correct minimum fuel usage is: ", result_part_two)
