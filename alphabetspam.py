ord = input()
ord_lista = list(ord)

summa_tot = 0
summa_space = 0
summa_lower = 0
summa_upper = 0
for i in ord_lista:
    
    summa_tot += 1

    if i == '_':
        summa_space += 1

    if i.islower() == True:
        summa_lower += 1
    
    if i.isupper() == True:
        summa_upper += 1

print(summa_space/summa_tot)
print(summa_lower/summa_tot)
print(summa_upper/summa_tot)
print((summa_tot-summa_space-summa_lower-summa_upper)/summa_tot)

   