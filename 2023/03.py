"""Day 3."""
import math
import sys

from collections import defaultdict

text = sys.stdin.read()
lines = text.splitlines()
n_rows = len(lines)
n_cols = len(lines[0])


def is_next_to_symbol(i: int, j: int) -> bool:
    for row in [-1, 0, 1]:
        for col in [-1, 0, 1]:
            x = i + row
            y = j + col
            if (
                x in range(n_rows)
                and y in range(n_cols)
                and not lines[x][y].isdigit()
                and lines[x][y] != "."
            ):
                return True
    return False


def is_next_to_gear(i: int, j: int) -> list[tuple[int, int]]:
    next_to = []
    for row in [-1, 0, 1]:
        for col in [-1, 0, 1]:
            x = i + row
            y = j + col
            if x in range(n_rows) and y in range(n_cols) and lines[x][y] == "*":
                next_to.append((x, y))
    return next_to


gears: defaultdict[tuple[int, int], list] = defaultdict(list)
ans1 = 0
for i, line in enumerate(lines):
    num = ""
    ok = False
    gears_next_to = set()
    for j, c in enumerate(line):
        if c.isdigit():
            num += c
            if is_next_to_symbol(i, j):
                ok = True
            if gear := is_next_to_gear(i, j):
                gears_next_to.update(gear)
        elif ok:
            ans1 += int(num)
            for gear in gears_next_to:
                gears[gear].append(int(num))

            ok = False
            num = ""
            gears_next_to.clear()
        else:
            num = ""
            gears_next_to.clear()

    if ok:
        ans1 += int(num)
        for gear in gears_next_to:
            gears[gear].append(int(num))

print("part1:", ans1)
ans2 = sum([math.prod(nums) for nums in gears.values() if len(nums) == 2])
print("part2:", ans2)
