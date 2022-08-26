
n = int(input())

lines = list()
for line in range(n):
    x = input().split()

    lines.append(x)

for i in range(n):
    testa = lines[i]
    
    if int(testa[1]) - int(testa[2]) > int(testa[0]):
        print('advertise')
    if int(testa[1]) - int(testa[2]) == int(testa[0]):
        print('does not matter')
    if int(testa[1]) - int(testa[2]) < int(testa[0]):
        print('do not advertise')



