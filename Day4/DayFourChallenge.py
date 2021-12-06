import numpy as np


def part_one():
    with open("Input.txt") as file:
        numbers_drawn = file.readline().split(",")

        data = np.loadtxt("Input.txt", skiprows=2)
        list_of_boards = np.array(np.split(data, len(data) / 5))
        list_of_markers = np.full_like(list_of_boards, False, dtype=bool)

        # Boolean array indexing: https://numpy.org/doc/stable/reference/arrays.indexing.html#boolean-array-indexing

        for number in numbers_drawn:
            list_of_markers[list_of_boards == int(number)] = True
            # Axis 1 = Zeile
            # Axis 0 = Spalte
            counter = 0
            for marker_board in list_of_markers:
                solved_horizontal = np.all(marker_board, axis=1)
                solved_vertical = np.all(marker_board, axis=0)
                is_solved_horizontal = np.any(solved_horizontal, axis=0)
                is_solved_vertical = np.any(solved_vertical, axis=0)
                if (is_solved_horizontal or is_solved_vertical):
                    board = list_of_boards[counter]
                    board[marker_board == True] = 0
                    sum_unmarked = np.sum(board)
                    result = sum_unmarked * int(number)
                    return result
                counter += 1


result_part_one = part_one()
print("The result of the first winning board is: ", result_part_one)


def part_two():
    with open("Input.txt") as file:
        numbers_drawn = file.readline().split(",")

        data = np.loadtxt("Input.txt", skiprows=2)
        list_of_boards = np.array(np.split(data, len(data) / 5))
        list_of_markers = np.full_like(list_of_boards, False, dtype=bool)

        last_winning_board = np.zeros((5, 5))
        last_winning_number = -1
        last_winning_marker_board = np.full_like(last_winning_board, False, dtype=bool)
        # Boolean array indexing: https://numpy.org/doc/stable/reference/arrays.indexing.html#boolean-array-indexing
        for number in numbers_drawn:

            list_of_markers[list_of_boards == int(number)] = True
            counter = 0
            for marker_board in list_of_markers:
                solved_horizontal = np.all(marker_board, axis=1)
                solved_vertical = np.all(marker_board, axis=0)
                is_solved_horizontal = np.any(solved_horizontal, axis=0)
                is_solved_vertical = np.any(solved_vertical, axis=0)
                if (is_solved_horizontal or is_solved_vertical):
                    # Create copys to avoid call by reference, when reference is set to None
                    last_winning_board = np.copy(list_of_boards[counter])
                    last_winning_number = number
                    last_winning_marker_board = np.copy(marker_board)
                    # Set all solved boards to None, to stop the board from calculating more.
                    list_of_boards[counter] = None
                    list_of_markers[counter] = None
                counter += 1

        last_winning_board[last_winning_marker_board == True] = 0
        sum_unmarked = np.sum(last_winning_board)
        result = sum_unmarked * int(last_winning_number)
        return result


result_part_two = part_two()
print("The score of the last winning board is: ", result_part_two)
