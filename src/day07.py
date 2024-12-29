from common import read_input
from dataclasses import dataclass
from typing import List


@dataclass
class Entry:
    target: int
    elems: List[int]


def parse(file):
    input = read_input(file)
    lines = []
    for line in input:
        res, nums = line.split(":")
        lines.append(Entry(int(res), [int(x) for x in nums.split(" ") if x != ""]))
    return lines


def isPossiblePart1(target: int, elems: List[int]) -> bool:
    curr = elems.pop()
    if target == curr:
        return True
    if len(elems) == 0:
        return False
    if target % curr != 0:
        return isPossiblePart1(target - curr, elems.copy())
    return isPossiblePart1(target / curr, elems.copy()) or isPossiblePart1(
        target - curr, elems.copy()
    )


def part1():
    data = parse("day07.txt")
    return sum(x.target for x in data if isPossiblePart1(x.target, x.elems))


def concatenate(n1, n2):
    return int(f"{n1}{n2}")


def isPossiblePart2(target: int, acc: int, elems: List[int]) -> bool:
    if acc == target and len(elems) == 0:
        return True
    if acc > target:
        return False
    if len(elems) == 0:
        return False
    curr = elems.pop(0)
    if acc == 0:
        return isPossiblePart2(target, curr, elems)
    return (
        isPossiblePart2(target, acc + curr, elems.copy())
        or isPossiblePart2(target, acc * curr, elems.copy())
        or isPossiblePart2(target, concatenate(acc, curr), elems.copy())
    )


def part2():
    data = parse("day07.txt")
    return sum(x.target for x in data if isPossiblePart2(x.target, 0, x.elems))


print(f"PART 1: {part1()}")
print(f"PART 2: {part2()}")
