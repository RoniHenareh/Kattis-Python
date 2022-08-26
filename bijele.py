tal = input().split()

rättsvar = [1, 1, 2, 2, 2, 8]

for j in range(len(rättsvar)):
    svar = rättsvar[j] - int(tal[j])

    print(svar, end = ' ')
print('')


