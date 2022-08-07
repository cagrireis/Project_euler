a = 1
b = 1
liste = []
while (b < 4000000):
    a, b = b, b + a
    if (b % 2 == 0):
        liste.append(b)
toplam = 0
for element in liste:
    toplam = toplam + element
print(toplam)