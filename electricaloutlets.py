import sys

n = int(input())

lista = list()
for line in range(n):
    tal = input().split()
    lista.append(tal)
    
for i in lista:
    m = int(i[0])

    sum = 0
    for j in range(1, m+1):
        sum += int(i[j])

    k = m-1

    print(sum-k)
    

