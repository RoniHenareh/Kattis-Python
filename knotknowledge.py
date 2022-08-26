n = int(input())

knut_learn = input().split()
knut_know = input().split()

for i in range(n):
    
    if knut_learn[i] not in knut_know: 
        print(knut_learn[i])

