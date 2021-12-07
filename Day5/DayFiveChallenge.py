import numpy as np


def part_one():
    with open("Input.txt") as file:
        content = file.read().splitlines()
        new_content = [list(map(int, line.replace(" -> ", ",").split(","))) for line in content]
        lines_array = np.zeros((999, 999))
        for coordinates in new_content:
            mark_positions_between(lines_array, coordinates[0], coordinates[2], coordinates[1], coordinates[3], False)

        result_matrix = np.where(lines_array > 1, 1, 0)
        result = np.sum(result_matrix)
        return result


def mark_positions_between(array, x1, x2, y1, y2, diagonals):
    if x1 == x2:
        # create step forward or backwards
        step = +1 if y1 < y2 else -1
        for i in range(y1, y2 + step, step):
            array[x1, i] += 1
    elif y1 == y2:
        # create step forward or backwards
        step = +1 if x1 < x2 else -1
        for i in range(x1, x2 + step, step):
            array[i, y1] += 1
    else:
        if diagonals:
            step_horizontal = +1 if x1 < x2 else -1
            step_vertical = step = +1 if y1 < y2 else -1
            j = y1
            for i in range(x1, x2 + step_horizontal, step_horizontal):
                array[i, j] += 1
                j += step_vertical


result_part_one = part_one()
print("Result one is: ", result_part_one)


def part_two():
    with open("Input.txt") as file:
        content = file.read().splitlines()
        new_content = [list(map(int, line.replace(" -> ", ",").split(","))) for line in content]
        lines_array = np.zeros((999, 999))
        for coordinates in new_content:
            mark_positions_between(lines_array, coordinates[0], coordinates[2], coordinates[1], coordinates[3], True)

        print(lines_array)

        result_matrix = np.where(lines_array > 1, 1, 0)
        result = np.sum(result_matrix)
        return result


result_part_two = part_two()
print(result_part_two)
