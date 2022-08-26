
ord = input()
ord_lista = list(ord)

#print(ord_lista)

# nu vill vi kolla tre bokstäver i taget

ny_ord_lista = list()

start = 0
slut = len(ord_lista) // 3

while slut >= 1:

    ny_ord_lista.append(ord_lista[start:start + 3])

    slut -= 1
    start += 3

#print(ny_ord_lista)

summa = 0
for delen in ny_ord_lista:

    if delen[0] != 'P':
        summa += 1
    if delen[1] != 'E':
        summa += 1
    if delen[2] != 'R':
        summa += 1

print(summa)



