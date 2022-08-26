tal = input().split()

h = int(tal[0])
v = int(tal[1])

import math

svar = (h / math.sin(math.radians(v)))

print(math.ceil(svar))