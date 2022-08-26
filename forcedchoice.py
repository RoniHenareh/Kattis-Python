
tal = input().split()

n = int(tal[0]) # antal kort
p = int(tal[1]) # secret prediction
s = int(tal[2]) # number of steps, rader

for i in range(s):
    
    svar = 0 # återställer

    val = input().split()
    valint = list(map(int, val))

    m = valint[0]

    for i in range(1, m + 1):

        if valint[i] == p:
            svar += 1

    if svar > 0:
        print('KEEP')
    else:
        print('REMOVE')
                    
        