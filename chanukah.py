n = int(input())

lines = list()
for line in range(n):
    tal = input().split()
    lines.append(tal)

print(lines)

for i in lines:
    sum = 0
    n = int(i[1])
    for j in range(1, n+1):
        sum += j
    print(int(i[0]), sum+n)


