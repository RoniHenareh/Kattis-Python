n = int(input())

for i in range(n):

    antal_städer = int(input())

    städer = list()
    for i in range(antal_städer):

        stad = input()
        städer.append(stad)
    print(len(set(städer)))

