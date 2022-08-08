n = 2
m = 1
while (True):
    liste = []
    if (m == 10001):
        print(n)
        break
    n = n + 1
    for i in range(1, n + 1):
        if (n % i == 0):
            liste.append(i)
    if (len(liste) == 2):
        m = m + 1