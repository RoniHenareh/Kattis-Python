
names = input()
lista_namn = list(names)
#print(lista_namn)

förkortning = list()

for letter in lista_namn:
    if letter.isupper() == True:
        förkortning.append(letter)

svar = ''
for i in förkortning:
    svar = svar + i
print(svar)

#print(förkortning)
