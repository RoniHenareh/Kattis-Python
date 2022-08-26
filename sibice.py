import math

tal = input().split()

N = int(tal[0])
W = int(tal[1])
H = int(tal[2])

#print(tal)

lista = list()
for i in range(N):
    svar = input()
    lista.append(svar)
#print(lista) # läng av varje tändsticka

for i in lista:

    if int(i) <= H or int(i) <= math.sqrt((math.pow(H, 2) + math.pow(W, 2))) :
        print('DA')
    else:
        print('NE')

