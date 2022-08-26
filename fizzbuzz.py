tal = input().split()

x = int(tal[0])
y = int(tal[1])
n = int(tal[2])

for i in range(1, n+1):

    if (i % x) == 0 and (i % y) == 0:
        print('FizzBuzz')
    elif (i % x) == 0:
        print('Fizz')
    elif (i % y) == 0:
        print('buzz')
    else:
        print(i)