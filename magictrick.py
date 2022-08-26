ord = input()
lista = list(ord)
sett = set(lista)

if len(lista) > len(sett):
    print(0)
else:
    print(1)