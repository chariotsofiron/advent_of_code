"""Day 1."""
import sys

text = sys.stdin.read()

nums = "one two three four five six seven eight nine".split()

total = 0
for line in text.splitlines():
    digits = []
    for i, char in enumerate(line):
        if char.isdigit():
            digits.append(int(char))
            continue
        for j, num in enumerate(nums, start=1):
            if line[i:].startswith(num):
                digits.append(j)
                break
    total += digits[0] * 10 + digits[-1]
print(total)
