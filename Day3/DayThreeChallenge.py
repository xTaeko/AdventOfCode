import numpy as np

maximal_values = None
minimal_values = None
binarys = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]


def part_one():
    zeros = np.zeros((12,), dtype=int)
    ones = np.zeros((12,), dtype=int)
    with open("Input.txt") as file:
        content = file.readlines()

        for line in content:
            counter = 0
            for letter in line:
                if letter == "0":
                    zeros[counter] += 1
                elif letter == "1":
                    ones[counter] += 1
                counter += 1

        zipped = list(zip(zeros, ones))

        maximal_values = [0 if a > b else 1 for a, b in zipped]
        minimal_values = [1 if a > b else 0 for a, b in zipped]

        gammarate = int("".join(str(element) for element in maximal_values), 2)

        epsilonrate = int("".join(str(element) for element in minimal_values), 2)

        result = gammarate * epsilonrate
        print(result)


part_one()


def part_two():
    # Oxygen Generator rating
    zeros = np.zeros((12,), dtype=int)
    ones = np.zeros((12,), dtype=int)
    with open("Input.txt") as file:
        content = file.read().splitlines()

        result_oxygen = define_values_recursive(content, 0, True)
        oxygen_binary_list = [a * int(b) for a, b in zip(binarys, list(result_oxygen))]
        oxygen = sum(oxygen_binary_list)

        result_co2 = define_values_recursive(content, 0, False)
        co2_binary_list = [a * int(b) for a, b in zip(binarys, list(result_co2))]
        co2 = sum(co2_binary_list)

        result = oxygen * co2
        print(result)


def define_values_recursive(content, column_number, oxygen):
    if len(content) == 1:
        return content[0]
    zeros = 0
    ones = 0
    for line in content:
        letter = line[column_number]
        if letter == "0":
            zeros += 1
        elif letter == "1":
            ones += 1

    if (oxygen):
        compare_value = "1" if ones >= zeros else "0"
    else:
        compare_value = "0" if zeros <= ones else "1"

    new_content = [line for line in content if line[column_number] == compare_value]
    return define_values_recursive(new_content, column_number + 1, oxygen)


part_two()
