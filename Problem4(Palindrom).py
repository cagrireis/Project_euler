liste1 = []
liste2 = []
for i in range(100, 1001):
    for k in range(100, 1001):
        liste1.append(i * k)
for element in liste1:
    if (len(str(element)) == 5):
        if (str(element)[:3] == str(element)[:2:-1]):
            liste2.append(element)
    elif (len(str(element)) == 6):
        if (str(element)[0:3] == str(element)[:2:-1]):
            liste2.append(element)
    elif (len(str(element)) == 7):
        if (str(element)[:4] == str(element)[:2:-1]):
            liste2.append(element)
    else:
        print("ERROR")
liste2.sort()
print(liste2[len(liste2) - 1])