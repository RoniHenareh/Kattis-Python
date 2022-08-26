tal = input()
tal_lista = list(tal)
tal_lista.remove('-')

#print(tal_lista)
tal_lista = list(map(int, tal_lista))
#print(tal_lista)

summa = 4*tal_lista[0] + 3*tal_lista[1] + 2*tal_lista[2] + 7*tal_lista[3] + 6*tal_lista[4] + 5*tal_lista[5] + 4*tal_lista[6] + 3*tal_lista[7] + 2*tal_lista[8] + 1*tal_lista[9]

if (summa % 11) == 0:
    print(1)
else:
    print(0)