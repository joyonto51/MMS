inp=input("Enter the radius of  circle:")
r=int(inp)
inp=input("Enter the Arm of square:")
a=int(inp)
A=2*3.1416*(r*r)
B=a*a

if A>=B:
     print("This is possibe")
else:
     print("This is impossible")
