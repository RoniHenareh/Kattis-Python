
tal = input()

lista = list(tal)

tal1 = lista[0]
tal2 = lista[1]

lista[0] = tal2
lista[1] = tal1

sum = ''
for i in lista:
    sum += i
print(int(sum))