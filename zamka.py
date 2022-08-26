l = int(input())
d = int(input())
x = int(input())

svar = list()
for i in range(l, d + 1): 
    
    sum1 = 0
    sum1 += i
    #print('sum1', sum1)
    lista1 = list(str(sum1))
    #print('lista1', lista1)
    
    sum2 = 0
    for i in lista1:
        
        sum2 += int(i)
    #print('sum2', sum2)

    if sum2 == x:
        svar.append(sum1)

svar.sort()
print(svar[0])
print(svar[-1])