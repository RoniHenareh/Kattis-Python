hej = input()

lista = list()

for i in hej:
    lista.append(i)
#print(lista)

n = lista[1:-1]

for i in range(1, len(n)+1):

    lista.insert(1, 'e')

svar = ''
for i in lista:
    svar += i

print(svar)
