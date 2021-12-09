import numpy as np


def part_one():
    with open("Input.txt") as file:
        input = file.read().splitlines()
        content = [[numbers.strip().split(" ") for numbers in line.split("|")] for line in input]
        unique_segment_numbers = 0
        for entry in content:
            for digit in entry[1]:
                if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
                    unique_segment_numbers += 1
        return unique_segment_numbers


result_part_one = part_one()
print("Numbers with unique segments: ", result_part_one)


#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg


def part_two():
    with open("Input.txt") as file:
        input = file.read().splitlines()
        content = [[numbers.strip().split(" ") for numbers in line.split("|")] for line in input]
        overall_result = 0
        for entry in content:
            numbers = np.empty(10, dtype=object)
            leftovers_with5 = []
            leftovers_with6 = []
            for digit in entry[0]:
                if len(digit) == 2:
                    numbers[1] = digit
                elif len(digit) == 4:
                    numbers[4] = digit
                elif len(digit) == 3:
                    numbers[7] = digit
                elif len(digit) == 7:
                    numbers[8] = digit
                elif len(digit) == 5:
                    leftovers_with5.append(digit)
                elif len(digit) == 6:
                    leftovers_with6.append(digit)

            tmp_segment_f = ""
            # Six is the only 6 segment value not containing the whole segments of 1 & Calculate Segment F
            for six_segment_number in leftovers_with6:
                differencemap = set(six_segment_number) - set(numbers[1])
                if len(differencemap) == 5:
                    numbers[6] = six_segment_number
                    tmp_segment_f = [item for item in numbers[1] if item in six_segment_number][0]
                    leftovers_with6.remove(six_segment_number)
                    break

            # Three is the only 5 segment value containing the whole segments of 1
            # Five Segment Number with Segment F in it is 5, the other is 2
            for five_segment_number in leftovers_with5:
                differencemap = set(five_segment_number) - set(numbers[1])
                if (len(differencemap) == 3):
                    numbers[3] = five_segment_number
                elif tmp_segment_f in five_segment_number:
                    numbers[5] = five_segment_number
                elif tmp_segment_f not in five_segment_number:
                    numbers[2] = five_segment_number

            # Calculate Segment E
            tmp_segment_e = (set(numbers[6]) - set(numbers[5])).pop()

            # Six Segment Number with Segment E in it is 0, the other is 9
            for six_segment_number in leftovers_with6:
                if tmp_segment_e in six_segment_number:
                    numbers[0] = six_segment_number
                else:
                    numbers[9] = six_segment_number

            # Get the result of the four output digits
            results = list(numbers)
            print(results)

            result_string = ""
            for number in entry[1]:
                for result in results:
                    if set(number) == set(result):
                        result_string += str(results.index(result))
                        break

            overall_result += int(result_string)

    return overall_result


result_part_two = part_two()
print("The sum of all values is: ", result_part_two)
