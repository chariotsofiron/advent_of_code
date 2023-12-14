"""Day 4."""
import sys
from collections import defaultdict

text = sys.stdin.read()
lines = text.splitlines()
n_rows = len(lines)
n_cols = len(lines[0])


scores = {}
n_cards = defaultdict(int)

ans1 = 0
for i, line in enumerate(lines, start=1):
    blah = line.split(":")[1]
    left, right = blah.split("|")
    winning = set(left.split())
    mine = right.split()

    score = sum(card in winning for card in mine)
    scores[i] = score

    n_cards[i] += 1
    for j in range(score):
        n_cards[i + 1 + j] += n_cards[i]

ans1 = sum(2 ** (x - 1) for x in scores.values() if x != 0)
ans2 = sum(n_cards.values())

print("part1:", ans1)
print("part2:", ans2)
