from common import read_input


def parse(file):
    input = read_input(file)
    lines = []
    for line in input:
        lines.append([int(x) for x in line.split(" ")])
    return lines


def makeSublists(list):
    sublists = []
    for i, n in enumerate(list):
        if i == 0:
            sublists.append(list[1:])
            continue
        if i == len(list) - 1:
            sublists.append(list[:i])
            continue
        sublist = list[:i] + list[i + 1 :]
        sublists.append(sublist)
    return sublists


def isIncreasing(line, part2=False, recursed=False):
    for i, n in enumerate(line):
        if i == len(line) - 1:
            return True
        diff = line[i + 1] - n
        if diff > 3 or diff < 1:
            if part2 and not recursed:
                return any(isIncreasing(x, True, True) for x in makeSublists(line))
            return False


def valid(line, part2=False):
    rev = line.copy()
    rev.reverse()
    return isIncreasing(line, part2) or isIncreasing(rev, part2)


data = parse("day02.txt")


def part1():
    return sum(1 for x in data if valid(x))


def part2():
    return sum(1 for x in data if valid(x, True))


print(f"PART 1: {part1()}")
print(f"PART 2: {part2()}")
