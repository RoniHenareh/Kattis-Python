tal = input().split()

r1 = int(tal[0])
s = int(tal[1])

def beräkna_r2(r1, s):
    r2 = 2*s-r1
    return r2

print(beräkna_r2(r1, s))