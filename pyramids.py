n = int(input()) # blocks available

def pyramid(n):

    sum = 1

    i = 3
    j = 1
    
    while n >= sum:

        #print(start)
        #print(sum1)

        sum += (i**2)
        
        i += 2
        j += 1

    print(j-1)
   

pyramid(n)