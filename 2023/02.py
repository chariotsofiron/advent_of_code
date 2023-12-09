"""Day 2."""
import sys
import math

text = sys.stdin.read()

max_allowed = {"red": 12, "green": 13, "blue": 14}

ans1 = 0
ans2 = 0
for i, game in enumerate(text.splitlines(), start=1):
    line = game.split(":")[1]
    ok = True
    maxes = {}
    for event in line.split(";"):
        for thing in event.split(","):
            count, color = thing.strip().split()
            maxes[color] = max(maxes.get(color, 0), int(count))
            if int(count) > max_allowed[color]:
                ok = False
    ans2 += math.prod(maxes.values())
    if ok:
        ans1 += i

print("part1:", ans1)
print("part2:", ans2)
