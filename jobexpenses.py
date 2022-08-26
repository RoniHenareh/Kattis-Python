n = int(input())

# incomes as positive integers 
# expenses as negative integers

pengar = input().split()
tal = list(map(int, pengar))

intäkter = list()
kostnader = list()

for i in tal:
    
    if i > 0:
        intäkter.append(i)
    else:
        kostnader.append(i)

if len(kostnader) > 0:
    print(-sum(kostnader))
else:
    print(0)
    