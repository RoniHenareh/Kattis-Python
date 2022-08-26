import sys

N = int(input())

lines = list()
for line in sys.stdin.readlines():
    line = line.strip("\n")
    lines.append(int(line))
    
print(N)
print(lines)

sum = 0
for line in lines:
    sum += line

n = N-1
print(sum-n)