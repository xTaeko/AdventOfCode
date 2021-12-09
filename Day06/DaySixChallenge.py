import numpy as np


def part_one():
    with open("Input.txt") as file:
        input = file.read().splitlines()
        # Create List of splittet values, afterwards use list comprehension for using int function over all of them. Unpack list afterwards
        content = [[int(item) for item in line.split(",")] for line in input][0]

        # One Day
        for day in range(0, 80):
            calculate_One_Day(content)
        return len(content)


def calculate_One_Day(laternfish_counter):
    for counter_index in range(0, len(laternfish_counter)):
        if laternfish_counter[counter_index] == 0:
            laternfish_counter[counter_index] = 6
            laternfish_counter.append(8)
        else:
            laternfish_counter[counter_index] -= 1


result_part_one = part_one()
print("Laternfishes after 80 Days: ", result_part_one)


def part_two():
    with open("Input.txt") as file:
        input = file.read().splitlines()
        # Create List of splittet values, afterwards use list comprehension for using int function over all of them. Unpack list afterwards
        content = [[int(item) for item in line.split(",")] for line in input][0]
        current_state = np.zeros(9)
        for fish in content:
            current_state[fish] += 1

        for day in range(0, 256):
            tmp_list = np.zeros(9)
            for index in range(len(current_state) - 1, -1, -1):
                if index == 0:
                    tmp_list[index] = current_state[index + 1]
                    tmp_list[6] += current_state[index]
                    tmp_list[8] += current_state[index]
                elif index == 8:
                    tmp_list[index] = 0
                else:
                    tmp_list[index] = current_state[index + 1]
            current_state, tmp_list = tmp_list, current_state

            result = np.sum(current_state)
        return result


result_part_two = part_two()
print("Laternfishes after 256 Days: ", result_part_two)
