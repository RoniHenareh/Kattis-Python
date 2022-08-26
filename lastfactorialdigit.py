n = int(input())

for i in range(n):
    tal = int(input())
    
    sum = 1
    for i in range(2, tal + 1):
        sum *= i
        
    lista = list(str(sum))
    
    print(lista[-1])
    