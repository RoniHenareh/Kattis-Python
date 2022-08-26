tal = input().split()

tal1 = tal[0]
tal2 = tal[1]

tal1_lista = list(tal1)
del11 = tal1_lista[0]
del12 = tal1_lista[2]
tal1_lista[0] = del12
tal1_lista[2] = del11

tal2_lista = list(tal2)
del21 = tal2_lista[0]
del22 = tal2_lista[2]
tal2_lista[0] = del22
tal2_lista[2] = del21

sum1 = ''
for i in tal1_lista:
    sum1 += i

sum2 = ''
for j in tal2_lista:
    sum2 += j

if int(sum1) > int(sum2):
    print(int(sum1))
else:
    print(int(sum2))


