värden = input()
värden_list = list(värden)

T = 0
C = 0
G = 0

for i in värden_list:
    
    if i == 'T':
        T += 1
        
    if i == 'C':
        C += 1
        
    if i == 'G':
        G += 1
     
sum = 0
sum += (T**2) + (C**2) + (G**2)

while T > 0 and C > 0 and G > 0:

    sum += 7
    T -= 1
    C -= 1
    G -= 1
    
print(sum)



    
    