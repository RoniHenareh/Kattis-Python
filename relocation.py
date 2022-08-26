tal = input().split()

n = int(tal[0])
q = int(tal[1])

# företag vi följer
location_track = input().split()
location_list = list()
for i in range(n):
    location_list.append(int(location_track[i]))

dic = dict()

for i in range(n):
    dic[i+1] = location_list[i]

for i in range(q):

    talen = input().split()

    if int(talen[0]) == 1:

        dic[int(talen[1])] = int(talen[2])
    
    else:

        print(abs(dic[int(talen[1])]-dic[int(talen[2])]))








