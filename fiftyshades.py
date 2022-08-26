n = int(input())

summa = 0
for i in range(n):
    
    ord = input()
    ord_lista = list(ord)
    
    omvandla = (map(lambda x: x.lower(), ord_lista)) # lambda arguments : expression
    ny_lista = ''.join(list(omvandla)) 

    if 'pink' in ny_lista or 'rose' in ny_lista:
        summa += 1

if summa > 0:
    print(summa)
else:
    print('I must watch Star Wars with my daughter')
    