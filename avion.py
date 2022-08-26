antal = 0
for i in range(1, 6):
    
    skylt = input()
    #print(i)

    if 'FBI' in skylt:
        print(i, end=' ')
        antal += 1

print('')

if antal == 0:
    print('HE GOT AWAY!')