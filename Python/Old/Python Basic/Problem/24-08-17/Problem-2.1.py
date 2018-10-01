inp=input("Enter the value of A:")
a=int(inp)
inp=input("Enter the value of B:")
b=int(inp)

c=a-b

if c<=0:
    print("The Equation is:"+str(c*-1))

else:
    print("the Equation is:"+str(c))