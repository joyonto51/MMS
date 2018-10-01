a=float(input("Enter a value:"))

A=a%1
b=int(a)
if A<0.5:
    print("the number is:"+str(b))
elif A>=0.5:
    print("The number is:"+str(b+1))

