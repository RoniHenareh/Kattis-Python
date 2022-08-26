tal = input().split()

n = int(tal[0]) # hela sidan
h = int(tal[1])
v = int(tal[2])

v1 = 4 * h * v
v2 = 4 * h * (n-v)
v3 = 4 * (n-h) * v
v4 = 4 * (n-h) * (n-v)

lista = [v1, v2, v3, v4]

print(max(lista))

