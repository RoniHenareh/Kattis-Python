rad1 = input()
rad2 = input()

rad1_lista = list(map(int, rad1))
rad2_lista = list(map(int, rad2))

summa = 0
for i in range(4):

    if rad1_lista[i] != rad2_lista[i]:
        summa += 1

print(2 ** summa)

# alt
#print(2**sum(a != b for a,b in zip(input(), input())))

