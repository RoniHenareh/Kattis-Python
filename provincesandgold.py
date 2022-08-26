
pengar = input().split()
lista = list(map(int, pengar)) # allt är ints

dic = {}

buyingpower = 0

if lista[0]:
    buyingpower += lista[0]*3

if lista[1]:
    buyingpower += lista[1]*2

if lista[2]:
    buyingpower += lista[2]*1

#print(buyingpower)

while True:
    if buyingpower >= 8:
        print('Province or Gold')
        break
    if buyingpower >= 6:
        print('Duchy or Gold')
        break
    if buyingpower >= 5:
        print('Duchy or Silver')
        break
    if buyingpower >= 3:
        print('Estate or Silver')
        break
    if buyingpower >= 2:
        print('Estate or Copper')
        break
    if buyingpower <= 1:
        print('Copper')
        break
    False













    