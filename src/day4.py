def checkOverlap(pair):
    sections = pair.split(',')
    cleaningRange1 = sections[0].split('-')
    cleaningRange2 = sections[1].split('-')
    if ((int(cleaningRange1[0]) <= int(cleaningRange2[0])
        and int(cleaningRange1[1]) >= int(cleaningRange2[1]))
        or (int(cleaningRange1[0]) >= int(cleaningRange2[0])
            and int(cleaningRange1[1]) <= int(cleaningRange2[1]))):
        return 2
    elif ((int(cleaningRange1[0]) >= int(cleaningRange2[0])
            and int(cleaningRange1[0]) <= int(cleaningRange2[1]))
            or (int(cleaningRange1[1]) >= int(cleaningRange2[0])
                and int(cleaningRange1[1]) <= int(cleaningRange2[1]))):
        return 1
    else:
        return 0
    

def part1(filename):
    file = open(filename, 'r')
    pairs = file.readlines()
    fullyEncompassedRanges = 0
    for pair in pairs:
        if checkOverlap(pair) == 2:
            fullyEncompassedRanges += 1
    return fullyEncompassedRanges


def part2(filename):
    file = open(filename, 'r')
    pairs = file.readlines()
    overlappingPairs = 0
    for pair in pairs:
        if checkOverlap(pair) > 0:
            overlappingPairs += 1
    return overlappingPairs


if __name__ == '__main__':
    print(f'The answer to part 1 is {part1("input/day4.txt")}')
    print(f'The answer to part 2 is {part2("input/day4.txt")}')
