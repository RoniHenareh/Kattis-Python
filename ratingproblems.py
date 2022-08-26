tal = input().split()

n = int(tal[0]) # tot domare
k = int(tal[1]) # domare som redan rÃ¶stat

sum = 0
for i in range(k):
    röster = int(input())
    sum += röster

if n == k:

    min = float(sum / n)
    max = float(sum / n)

    print(min, max)
    
else:
    
    röster_kvar = n - k

    min = float((sum + ((-3)*röster_kvar)) / n)
    max = float((sum + ((3)*röster_kvar)) / n)

    print(min, max)
