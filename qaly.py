
def qaly(n, lista):

    sum = 0

    for list in lista:
        sum += list[0]*list[1]
        if i == n:
            break
    return sum
   
n = input()
lista = list()
for i in range(int(n)):

    information = list(map(float, (input().split())))
    lista.append(information)

#print(n)
#print(lista)

test = qaly(n, lista)
print(test)