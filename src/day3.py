def part1(filename):
    file = open(filename, 'r')
    rucksacks = file.readlines()
    priority = 0
    for items in rucksacks:
        compartment1 = items[:len(items)//2]
        compartment2 = items[len(items)//2:]
        for item1 in compartment1:
            for item2 in compartment2:
                if item1 == item2:
                    if item1.isupper():
                        priority += ord(item1) - 38
                    elif item1.islower():
                        priority += ord(item1) - 96
                    break
            if item1 == item2:
                break
    file.close
    return priority


def part2(filename):
    file = open(filename, 'r')
    rucksacks = file.readlines()
    priority = 0
    count = 0
    rucksack2 = ''
    rucksack3 = ''
    for rucksack in rucksacks:
        count += 1
        if count == 3:
            count = 0
            for item1 in rucksack:
                for item2 in rucksack2:
                    if item1 == item2:
                        for item3 in rucksack3:
                            if item1 == item3:
                                if item1.isupper():
                                    priority += ord(item1) - 38
                                elif item1.islower():
                                    priority += ord(item1) - 96
                                break
                        if item1 == item3:
                            break
                if item1 == item2:
                    break
        rucksack3 = rucksack2
        rucksack2 = rucksack
    file.close
    return priority


if __name__ == '__main__':
    print(f'the answer to part 1 is {part1("input/day3.txt")}')
    print(f'the answer to part 2 is {part2("input/day3.txt")}')
