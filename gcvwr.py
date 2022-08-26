# GCVWR = max vikt + bilens vikt
# bör inte vara mer än 90 % 

vikter = input().split()
vikt1 = int(vikter[0])
vikt2 = int(vikter[1])
n = int(vikter[2])

saker = input().split()

max1 = int((vikt1 - vikt2) * 0.90)

sum = 0
for i in saker:
    sum += int(i)

svar = max1 - sum

print(svar)