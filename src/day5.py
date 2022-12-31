def fillInitialStacks(input, stacks):
    count = 0
    while count < len(input)//4:
        if (input[1 + 4 * count].isalpha()):
            stacks[count].append(input[1 + 4 * count])
        count += 1


def crateMover9000(move, fromStack, toStack, stacks):
    count = 0
    while count < move:
        stacks[toStack].append(stacks[fromStack].pop())
        count += 1


def crateMover9001(move, fromStack, toStack, stacks):
    count = 0
    tempStack = []
    while count < move:
        tempStack.append(stacks[fromStack].pop())
        count += 1
    while count > 0:
        stacks[toStack].append(tempStack.pop())
        count -= 1


def part1(filename):
    file = open(filename, 'r')
    inputs = file.readlines()
    stacks = []
    count = 0
    commandsStart = 0
    topCrates = ''
    while count < (len(inputs[0])//4):
        stacks.append([])
        count += 1
    for input in inputs:
        commandsStart += 1
        if input != '\n':
            fillInitialStacks(input, stacks)
        else:
            break
    for stack in stacks:
        stack.reverse()
    count = 0
    for input in inputs[commandsStart:]:
        command = input.split(" ")
        (crateMover9000(int(command[1]), int(command[3]) - 1,
                        int(command[5]) - 1, stacks))
    for stack in stacks:
        topCrates += stack[-1]
    file.close
    return topCrates


def part2(filename):
    file = open(filename, 'r')
    inputs = file.readlines()
    stacks = []
    count = 0
    commandsStart = 0
    topCrates = ''
    while count < (len(inputs[0])//4):
        stacks.append([])
        count += 1
    for input in inputs:
        commandsStart += 1
        if input != '\n':
            fillInitialStacks(input, stacks)
        else:
            break
    for stack in stacks:
        stack.reverse()
    count = 0
    for input in inputs[commandsStart:]:
        command = input.split(" ")
        (crateMover9001(int(command[1]), int(command[3]) - 1,
                        int(command[5]) - 1, stacks))
    for stack in stacks:
        topCrates += stack[-1]
    file.close
    return topCrates


if __name__ == '__main__':
    print(f'The answer to part 1 is {part1("input/day5.txt")}')
    print(f'The answer to part 2 is {part2("input/day5.txt")}')
