def part_one():
    depth = 0
    horizontal = 0
    with open("Input.txt") as file:
        content = file.readlines()
        for line in content:
            stringlist = line.split(sep=" ")
            direction = stringlist[0]
            value = int(stringlist[1])

            if direction == "forward":
                horizontal += value
            elif direction == "down":
                depth += value
            elif direction == "up":
                depth -= value
        result = depth * horizontal
        print("The Result of the first Part is: ", result)


part_one()


def part_two():
    depth = 0
    horizontal = 0
    aim = 0
    with open('Input.txt') as file:
        content = file.readlines()
        for line in content:
            stringlist = line.split(sep=" ")
            direction = stringlist[0]
            value = int(stringlist[1])

            if direction == "forward":
                horizontal += value
                depth += value * aim
            elif direction == "down":
                aim += value
            elif direction == "up":
                aim -= value
        result = depth * horizontal
    print("The Result of the second Part is: ", result)


part_two()
