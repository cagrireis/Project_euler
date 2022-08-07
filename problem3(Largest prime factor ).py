sayi = 600851475143
liste1 = []
liste3 = []
for i in range(1, sayi + 1):
    if (sayi % i == 0):
        liste1.append(i)
for k in liste1:
    liste2 = []
    for l in range(1, k + 1):
        if (k % l == 0):
            liste2.append(l)
    if (len(liste2) == 2):
        liste3.append(k)
liste3.sort()
print(liste3[len(liste3) - 1])