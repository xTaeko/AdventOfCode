def part_one():
    stack = []
    dictionary = {"(":")", "[":"]", "{":"}", "<":">"}
    dictionary_points = {")":3, "]":57, "}":1197, ">":25137}
    wrong_brackets = []
    with open("Input.txt") as file:
        content = file.read().splitlines()
        for line in content:
            for letter in line:
                if dictionary.keys().__contains__(letter):
                    stack.append(letter)
                else:
                    last_open_one = stack.pop()
                    corresponding_closed_one = dictionary.get(last_open_one)
                    if corresponding_closed_one != letter:
                        wrong_brackets.append(letter)
                        break
        # Calculate the score for all the brackets in the list.
        result = 0
        for bracket in wrong_brackets:
            result += dictionary_points.get(bracket)
        return result


result_part_one = part_one()
print(result_part_one)


def part_two():
    stack = []
    dictionary = {"(":")", "[":"]", "{":"}", "<":">"}
    dictionary_points = {"(":1, "[":2, "{":3, "<":4}
    open_stacks = []
    corrupt_line = False
    # Find every incomplete line and save the stack
    with open("Input.txt") as file:
        content = file.read().splitlines()
        for line in content:
            for letter in line:
                if dictionary.keys().__contains__(letter):
                    stack.append(letter)
                else:
                    last_open_one = stack.pop()
                    corresponding_closed_one = dictionary.get(last_open_one)
                    if corresponding_closed_one != letter:
                        corrupt_line = True
                        break
            # If it is not a corrupt line append it to the open stacks. Clean the Boolean and Stack in any case
            if (not corrupt_line):
                open_stacks.append(stack.copy())
            stack.clear()
            corrupt_line=False

        # Calculate the score for every open stack saved in the list.
        result_list = []
        for result_stack in open_stacks:
            tmp_result = 0
            result_stack.reverse()
            for bracket in result_stack:
                tmp_result *=  5
                tmp_result += dictionary_points.get(bracket)
            result_list.append(tmp_result)

        result_list.sort()
        return result_list[int(len(result_list)/2)]



result_part_two = part_two()
print(result_part_two)