
lista = list()
for i in range(1, 6):
    tal = input().split()
    tal = list(map(int, tal))
    
    lista.append(sum(tal))
    
vinnare = max(lista)

plats = 1
for i in range(len(lista)):

    if lista[i] == vinnare:
        plats += i

print(plats, vinnare)

