värden = input().split()

n = int(värden[0])*4
d = värden[1]

dominant = {'A':11, 'K':4, 'Q':3, 'J':20, 'T':10, '9':14, '8':0, '7':0}
ej_dominant = {'A':11, 'K':4, 'Q':3, 'J':2, 'T':10, '9':0, '8':0, '7':0}

talen = list()
for i in range(n):
    värden = input()
    lista = list(värden)
    talen.append(lista)

sum = 0
for i in talen:
    if i[1] == d:
        sum += dominant[i[0]]
    else:
        sum += ej_dominant[i[0]]
print(sum)