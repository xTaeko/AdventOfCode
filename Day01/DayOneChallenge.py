def part_one():
    increased = 0
    last_number = 170
    with open('Input.txt') as file:
        for line in file:
            tmp_number = int(line)
            if tmp_number > last_number:
                increased += 1
            last_number = tmp_number
    print("It increases: ", increased, "times.")


part_one()


def part_two():
    with open("Input.txt") as file:
        content = [int(line) for line in file]
        # A + B + C < B + C +D if A < D --> Only compare first and fourth item.
        zipped = zip(content, content[3:])
        result = sum(x < y for x, y in zipped)
        print("The Packages increases: ", result, "times.")


part_two()
