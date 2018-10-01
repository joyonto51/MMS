inp=input("Enter the radius of  circle:")
r=int(inp)
inp=input("Enter the Arm of square:")
a=int(inp)
A=2*r
B=1.414*a         #because, 2r=1.414

if A>=B:
     print("This is possibe")
else:
     print("This is impossible")
