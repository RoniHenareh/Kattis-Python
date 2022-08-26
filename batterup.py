
n = int(input())
tal = input().split()

sum = 0
fel = 0
for i in tal:
    if i == '-1':
        fel += 1
    else:
        sum += int(i)
    

svar = sum / (n-fel)
print(svar)