inp=input("Enter the First number of Hour:")
a=int(inp)
inp1=input("Enter the Second number of Hour:")
b=int(inp1)

if a>=b:
    A=(12-a)+b
    print("Time Difference: "+str(A)+" hours")

if b>a:
    B=a-b
    print("Time Defference: "+str(B*-1)+"hours")

else:
    print(" or  Time Defference: 0 hours")