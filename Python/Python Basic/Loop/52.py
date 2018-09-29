x=int(input("Enter a number:"))
y=int(input("Enter another number:"))
z=int(input("Enter another number:"))

if(x>=y|y>=z):
    print("the numbers are:",z,y,x)
elif(y>=x|x>=z):
    print("the numbers are:",z,x,y)
elif(y>=z|z>=x):
    print("The numbers are:",x,z,y)
elif(z>=x|x>=y):
    print("The numbers are:",y,x,z)
elif (x>=z|z>=y):
    print("The numbers are:", y, z, x)
else:
    print("The numbers are:",x,y,z)
