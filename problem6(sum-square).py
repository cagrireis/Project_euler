toplam1 = 0
toplam2 = 0
for i in range(1, 101):
    toplam1 = toplam1 + i ** 2
    toplam2 = toplam2 + i
prot = toplam2 ** 2
res = prot - toplam1
print("Sonuç: {0} - {1} = {2}".format(prot, toplam1, res))