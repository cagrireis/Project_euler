def fact(k):
    res = 1
    for i in range(1, k + 1):
        res = res * i
    return res
x = 1_000_000
liste = []
for i in range(3, x + 1):
    ret = 0
    for k in str(i):
        ret = ret + fact(int(k))
    if (ret == i):
        liste.append(i)
top = 0
for element in liste:
    top = top + element
print(top)