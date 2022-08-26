# prefix number is the first three digits 
# the line number is the last four digits

tal = input()
lista = list(tal)

#print(lista)

if lista[0:3] == ['5', '5', '5']:
    print(1)
else:
    print(0)