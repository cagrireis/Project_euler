def fib():
    a = 1
    b = 1
    sayi = 2
    while (True):
        x = a
        a = b
        b = x + b
        sayi = sayi + 1
        if (len(str(b)) == 1000):
            return sayi
print("Cevap: {0}.".format(fib()))