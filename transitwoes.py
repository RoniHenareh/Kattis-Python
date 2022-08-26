import sys

tider = input().split()

s = tider[0] # lämnar huset
t = tider[1] # skolan börjar
n = tider[2] # antal byten

lines = list()
for line in sys.stdin.readlines():
    line = line.strip("\n")
    lines.append(line)

#print(lines)

gå_tider = lines[0].split()
åka_tider = lines[1].split()
buss_tider = lines[2].split()

sum = 0
for i in range(int(n)):

    sum += int(gå_tider[i]) # första bussen

    if sum != int(buss_tider[i]) or sum != int(buss_tider[i]) / 2:
        sum += (int(buss_tider[i]) - sum) # tiden tills bussen kommer
        sum += int(åka_tider[i])
    else:
        sum += int(åka_tider[i])

sum += int(gå_tider[-1]) # från sista bussen till skolan

#print(sum)
if sum <= int(t):
    print('yes')
else:
    print('no')