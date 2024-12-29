from functools import cache

INITIAL = [20, 82084, 1650, 3, 346355, 363, 7975858, 0]


def splitStr(s):
    index = int(len(s) / 2)
    return s[:index], s[index:]


@cache
def transform(element):
    if element == 0:
        return [1]
    elStr = f"{element}"
    if len(elStr) % 2 == 0:
        [fst, snd] = splitStr(elStr)
        return [int(fst), int(snd)]
    return [element * 2024]


@cache
def count(element, round):
    if round == 0:
        return 1
    return sum(count(x, round - 1) for x in transform(element))


def part1():
    return sum(count(x, 25) for x in INITIAL)


def part2():
    return sum(count(x, 75) for x in INITIAL)


print(f"PART 1: {part1()}")
print(f"PART 2: {part2()}")
