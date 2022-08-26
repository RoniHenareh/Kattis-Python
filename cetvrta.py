
tal1 = input().split()
tal2 = input().split()
tal3 = input().split()

första_lista = list()
andra_lista = list()

första1 = int(tal1[0])
första_lista.append(första1)
första2 = int(tal2[0])
första_lista.append(första2)
första3 = int(tal3[0])
första_lista.append(första3)

andra1 = int(tal1[1])
första_lista.append(andra1)
andra2 = int(tal2[1])
andra_lista.append(andra2)
andra3 = int(tal3[1])
andra_lista.append(andra3)

def unique(lista):
    for i in lista:
        ny_lista = lista.remove(i)
        if i not in lista:
            return i

print(unique(första_lista), unique(andra_lista))



