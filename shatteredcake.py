w = int(input())

n = int(input())

w_list = list()
l_list = list()

for i in range(n):
    bitar = input().split()
    
    w_list.append(int(bitar[0]))
    l_list.append(int(bitar[1]))

sum = 0 
for i in range(n):
    sum += (w_list[i]*l_list[i])

l = (sum/w)

print(int(l))