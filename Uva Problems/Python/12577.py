t = 0
while True:

    t += 1
    a = str(input())
    if (a[0]!= '*'):
        if (a == "Hajj"):
            print("Case {}:".format(t), "Hajj-e-Akbar")

        if (a == "Umrah"):
            print("Case {}:".format(t), "Hajj-e-Asghar")

    else:
        break
