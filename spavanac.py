tid = input().split()

h = int(tid[0])
m = int(tid[1])

tal = 45

if tal > m:

    nytt_tal = tal-m

    if h > 0:
        h -= 1
    else:
        h = 24
        h -= 1
    
    m = 60
    m -= nytt_tal

    print(h, m)

elif m > tal:

    m -= tal

    print(h, m)



    
   