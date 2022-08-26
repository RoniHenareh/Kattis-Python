värden = input()

lista = list(värden)

for i in range(len(lista)):
    
    try:

        if lista[i] == ':' and lista [i+1] == ')':
            print(i)

        elif lista[i] == ':' and lista [i+1] == '-' and lista[i+2] == ')':
                print(i)
        
        elif lista[i] == ';' and lista[i+1] == '-' and lista[i+2] == ')':
            print(i)

    except IndexError as e:
        continue


