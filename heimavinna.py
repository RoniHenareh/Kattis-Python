
tal = input().split(';')

sum = 0
for i in tal:
    talen = (i.split('-'))

    if len(talen) > 1:
        sum += (int(talen[1])+1) - int(talen[0]) 
    else:
        sum += 1
print(sum)
    

            

