dim = input().split()
lista = list(map(int, dim))

if lista[0] > (lista[2]+1) and lista[1] > (lista[3]+1):
    print(1)
else:
    print(0)