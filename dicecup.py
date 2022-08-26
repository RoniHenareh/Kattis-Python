tal = input().split()

tal1 = int(tal[0])
tal2 = int(tal[1])

if tal1 == tal2:
    print(tal1+1)
elif tal1 > tal2:
    n = tal1 - tal2

    nytt_tal1 = tal2+1
    for i in range(n):
        print(nytt_tal1)
        nytt_tal1 += 1
    print(tal1+1)

elif tal1 < tal2:
    m = tal2-tal1

    nytt_tal2 = tal1+1
    for i in range(m):
        print(nytt_tal2)
        nytt_tal2 += 1
    print(tal2+1)