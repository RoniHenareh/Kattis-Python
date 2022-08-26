tal = int(input())

binary = str(format(tal, 'b'))

binary_list = list(binary)

binary_list.reverse()

sum = ''
for i in binary_list:
    sum += i

new_binary = int(sum, 2)
print(new_binary)
    
