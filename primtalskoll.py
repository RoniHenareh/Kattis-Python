
n = int(input())

talen = input().split()
#print(talen)

def smallestDivisor(n):
 
    # om delbart med 2
    if (n % 2 == 0):
        return 2
 
    # testar resten
    i = 3
    while (i * i <= n):

        # delbart
        if (n % i == 0):
            return i

        # stegar
        i += 2
 
    return n # minsta

for i in talen:
    print(smallestDivisor(int(i)))


