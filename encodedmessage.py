n = int(input())

import math

for i in range(n):
    
    ord = input()
    ord_lista = list(ord)

    siffra = int(math.sqrt(len(ord_lista))) # konstant

    start = siffra - 1
    
    summa = ''
    for i in range(start, -1, -1):

        for j in range(len(ord_lista)):

            try:
                summa += str(ord_lista[i])
                i += siffra
            except IndexError as e:
                e
                
    print(summa)


           

            
            





    
    

    

       