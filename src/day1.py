def top3(calories, big, bigger, biggest):
    if calories > biggest:
        big = bigger
        bigger = biggest
        biggest = calories
    elif calories > bigger:
        big = bigger
        bigger = calories
    elif calories > big:
        big = calories
    return big, bigger, biggest


def part1(filename):
    file = open(filename, 'r')
    bag = file.readlines()
    maxCalories = 0
    calories = 0
    for food in bag:
        if food != '\n':
            totalCalories = int(food)
            calories = totalCalories + calories
        else:
            if calories > maxCalories:
                maxCalories = calories
            calories = 0
    file.close
    return (maxCalories)


def part2(filename):
    file = open(filename, 'r')
    bag = file.readlines()
    biggest = 0
    bigger = 0
    big = 0
    calories = 0
    for food in bag:
        if food != '\n':
            totalCalories = int(food)
            calories = totalCalories + calories
        else:
            big, bigger, biggest = top3(calories, big, bigger, biggest)
            calories = 0
    file.close
    big, bigger, biggest = top3(calories, big, bigger, biggest)
    totalCalories = big + bigger + biggest
    return (totalCalories)


if __name__ == '__main__':
    print(f'part 1 answer is {part1("input/day1.txt")}')
    print(f'part 2 answer is {part2("input/day1.txt")}')
