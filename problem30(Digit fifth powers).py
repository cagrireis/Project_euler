def pro():

    liste = []

    for element in range(2, 1000000):
        sayi = 0

        for i in str(element):
            sayi = sayi + int(i) ** 5

        if (sayi == element):
            liste.append(sayi)

    return liste

toplam = 0
for p in pro():
    toplam = toplam + p

print("Liste: {0}'dır, toplamları ise; {1}'dır.".format(pro(), toplam))