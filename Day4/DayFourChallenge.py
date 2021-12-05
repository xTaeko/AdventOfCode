import numpy as np


def part_one():
    list_solved = []
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
                    print(result)
                    exit()
                counter += 1


part_one()


def part_two():
    print("TWO")
    # List of boards (100) - delete every that wins


part_two()
