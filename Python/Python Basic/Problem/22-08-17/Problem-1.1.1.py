inp=input("Plz enter an year:")
n=int(inp)

if (n%4==0 and (n%400==0 or n%100!=0)):
    print(str(n)+" is a Leap year")

else:
    print(str(n)+" is not a Leap year")


