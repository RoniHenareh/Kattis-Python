import sys
# BPM = 60*b / p

n = int(input())

lines = list()
for line in sys.stdin.readlines():
    line = line.strip("\n").split()
    lines.append(line)

#print(lines)

for i in range(n):
    b = int(lines[i][0])
    p = float(lines[i][1])
    
    bpm = 60*b/p
    print(bpm - 60/p, bpm, bpm + 60/p)


