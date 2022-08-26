mening = input()

lista = list(mening)

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

sum = 0
for i in lista:
    if i in vowels:
        sum += 1
print(sum)