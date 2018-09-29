inp=input("Enter the number of Days:")
a=int(inp)

y=a/365            #y= 1.23459
Y=int(y)           #Y= 1 year

x=a%365             #x=35
m=x/30              #m=35/30=1.23554(float)
M=int(m)            #M= 1 month

D=x%30              #D=35%30= 5 days

print(str(Y)+"year,"+str(M)+"Month,"+str(D)+"Days")
