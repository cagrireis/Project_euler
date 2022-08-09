def bolum():
    n = 1
    while (True):
        m = 0
        for i in range(1, 21):
            if (n % i == 0):
                m = m + 1
            if (m == 20):
                return n
        n = n + 1
print(bolum())