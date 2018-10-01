inp=input("Please enter a number:")
a=float(inp)
B=a%1

if B<0.5:
    b=int(a)
    print("the number is:"+str(b))

if B>=0.5:
    c=int(a)
    print("The number is:"+str(c+1))

else:
    d=int(a)
    print("The number is:"+str(d))

