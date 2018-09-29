while True:
    n = int(input())
    if n==0:
        break
    L=""
    for N in range(1,n+1):
        l=""
        if N//100>=1:
            l +="c"
            N=N%100
        if N>=90:
            l+="xc"
            N=N%90
        if N//50>=1:
            l+= "l"
            N=N%50
        if N>=40:
            l+="xl"
            N=N%40
        if N//10>=1 and N<40:
            l+=(N//10)*"x"
            N=N%10
        if N//5>=1 and N!=9:
            l+="v"
            N=N%5
        if N==49:
            l+="il"
        if N==9:
            l+="ix"
        if N==4:
            l+="iv"
        if N<=3:
            l+=N*"i"
        L+=l
    c=int(L.count("c"))
    l=int(L.count("l"))
    x=int(L.count("x"))
    v=int(L.count("v"))
    i=int(L.count("i"))
    print("{}: {} i, {} v, {} x, {} l, {} c".format(n,i,v,x,l,c))

