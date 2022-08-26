n = int(input())

import sys

lines = list()
for line in sys.stdin.readlines():
    line = line.strip("\n")
    lines.append(line)

for i in range(n):
    if i % 2 == 0:
        print(lines[i])
    