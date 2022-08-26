tal = input().split()
lista = list(map(int, tal))

import math

semiperimeter = (lista[0] + lista[1] + lista[2] + lista[3]) / 2

# Applying Brahmagupta's formula to get maximum area of quadrilateral
svar = math.sqrt((semiperimeter - lista[0]) * (semiperimeter - lista[1]) *(semiperimeter - lista[2]) *(semiperimeter - lista[3]))
print(float(svar))