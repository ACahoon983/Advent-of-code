def game(match):
    if ((match[0] == 'A' and match[2] == 'X')
            or (match[0] == 'B' and match[2] == 'Y')
            or (match[0] == 'C' and match[2] == 'Z')):
        return 3
    elif ((match[0] == 'A' and match[2] == 'Y')
            or (match[0] == 'B' and match[2] == 'Z')
            or (match[0] == 'C' and match[2] == 'X')):
        return 6
    elif ((match[0] == 'A' and match[2] == 'Z')
            or (match[0] == 'B' and match[2] == 'X')
            or (match[0] == 'C' and match[2] == 'Y')):
        return 0


def toPlay(match):
    if ((match[0] == 'A' and match[2] == 'Y')
            or (match[0] == 'B' and match[2] == 'X')
            or (match[0] == 'C' and match[2] == 'Z')):
        return 1
    elif ((match[0] == 'A' and match[2] == 'Z')
            or (match[0] == 'B' and match[2] == 'Y')
            or (match[0] == 'C' and match[2] == 'X')):
        return 2
    elif ((match[0] == 'A' and match[2] == 'X')
            or (match[0] == 'B' and match[2] == 'Z')
            or (match[0] == 'C' and match[2] == 'Y')):
        return 3


def part1(filename):
    file = open(filename, 'r')
    rockPaperScissors = file.readlines()
    totalScore = 0
    for match in rockPaperScissors:
        handScore = ord(match[2]) - 87
        totalScore += game(match) + handScore
    file.close
    return totalScore


def part2(filename):
    file = open(filename, 'r')
    rockPaperScissors = file.readlines()
    totalScore = 0
    for match in rockPaperScissors:
        matchScore = (ord(match[2]) - 88) * 3
        totalScore += toPlay(match) + matchScore
    file.close
    return totalScore


if __name__ == '__main__':
    print(f'part 1 answer is {part1("input/day2.txt")}')
    print(f'part 2 answer is {part2("input/day2.txt")}')
