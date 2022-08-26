saker = input()

lista_saker = list(saker)

index1 = len(lista_saker[0:lista_saker.index('(')])
index2 = len(lista_saker[lista_saker.index(')'):-1])

if index1 == index2:
    print('correct')
else:
    print('fix')

