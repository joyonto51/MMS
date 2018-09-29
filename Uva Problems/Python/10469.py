while True:
    try:
        A,B = map(int,input().split())
    except:
        break

    a = A^B
    print("{}".format(a))













