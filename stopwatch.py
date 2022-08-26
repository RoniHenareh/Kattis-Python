n = int(input())

import sys

lines = list()
for line in sys.stdin.readlines():
    line = line.strip("\n")
    lines.append(line)
    
#print(lines)

if len(lines) % 2 != 0:
    print('still running')

else:
    sum = 0
    första = 0
    andra = 1
    n = len(lines) / 2

    while n > 0:

        sum += (int(lines[andra]) - int(lines[första]))

        första += 2
        andra += 2

        n -= 1

    print(sum)