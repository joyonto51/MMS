inp=input("Please Enter an year:")
n=int(inp)
if n%4==0 and (n%400==0 or n%100!=0):
    print(str(n)+" is a Leap year")
    print("The next Leap year is:"+str(n+4))

else:
    print(str(n)+" is not leap year")
a=n+(4-n%4)
b=a+(4-a%4)
if(a%4==0 and (a%400==0 or a%100!=0)):
    print("The next Leap year is:"+str(a))
elif(b%4==0 and (b%400 or b%100!=0)):
    print("The next leap year is:",b)

