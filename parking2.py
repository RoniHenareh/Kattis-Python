t = int(input())

for i in range(t):
    n = int(input())
    p = input().split()
    lista_p = list(map(int, p))
    
    svar = max(lista_p) - min(lista_p)
    
    print(svar*2)