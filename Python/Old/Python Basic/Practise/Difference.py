def diff(a,b):
    if(a>=b):
        return(a-b)
    else:
        return(b-a)

x=int(input("Enter a value of a:"))
y=int(input("Enter the value of b:"))
print(diff(x,y))
