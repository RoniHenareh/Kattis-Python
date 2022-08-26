namn = input()

lista = list(namn)

sum = ''

sum += lista[0]

for i in range(len(lista)):

    try:
        första = lista[i]
        nästa = lista[i+1]
    except IndexError as e:
        pass

    if första == nästa:
        continue

    else:
        sum += nästa
    

print(sum)


