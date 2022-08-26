ord = input().split() # lista
ord_set = set(ord) # set

if len(ord) > len(ord_set):
    print('no')
else:
    print('yes')

