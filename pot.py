import sys

lines = list()
for line in sys.stdin.readlines():
    line = line.strip("\n")
    lines.append((line))

lista = list()

for j in lines:
    if len(j) == 1:
        lista.append(0)
    else:
        lista.append(int(j[:-1]))

#print(lista)

upphöjt = list()
for i in lines:
    #print(i[-1])
    upphöjt.append(int(i[-1]))

#print(upphöjt)

sum = 0
for i in range(len(upphöjt)):
    sum += lista[i] ** upphöjt[i]

print(sum)






