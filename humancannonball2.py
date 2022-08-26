n = int(input())

from cmath import cos
import sys

lines = list()
for line in sys.stdin.readlines():
    line = line.strip("\n")
    line = line.split()
    lines.append(line)

import math

def beräkna_faran(v0, phi, x, h1, h2):

    # beräkna tiden
    t = (x / (v0 * math.cos(math.radians(phi))))

    # höjden vid den tiden
    y = v0 * t * math.sin(math.radians(phi)) - (0.5 * 9.81 * math.pow(t, 2))

    if (h1+1) <= y and y <= (h2-1):
        print('Safe')
    else:
        print('Not Safe')

for line in lines:
    
    v0 = float(line[0])
    phi = float(line[1])
    x1 = float(line[2])
    h1 = float(line[3])
    h2 = float(line[4])


    beräkna_faran(v0, phi, x1, h1, h2)






    

