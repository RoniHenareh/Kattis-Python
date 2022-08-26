
# contarct: size of lawns, cost of seed per square metre

cost = float(input())
lawns = int(input())

lista = list()
for i in range(lawns):
    tal = input().split()
    lista.append(tal)

sum = 0
for j in lista:
    #print('j', j)
    sum += float(j[0])*float(j[1])
print((sum*cost))


