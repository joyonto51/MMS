while True:
    try:
        a,b = map(int,input().split())
    except:
        break
    c = a-b
    if a<b:
        c*=-1
    else:
        pass
    print("{}".format(c))
