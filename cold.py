tal = int(input())

flera_tal = input()

lista = list(flera_tal)

sum = 0
for i in lista:
    if i == '-':
        sum += 1
print(sum)