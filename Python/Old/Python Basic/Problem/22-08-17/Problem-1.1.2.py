inp=input("Plz enter an year:")
n=int(inp)

if n%4==0 and (n%400==0 or n%100!=0):
    print(str(n)+" is a Leap year")
    print("the next leap year is:"+ str(n+4))

else:
    print(str(n)+" is not a Leap year")
    for a in range(1,7,1):
       if (n+a)%4==0 and ((n+a)%400==0 or (n+a)%100!=0):
          print("The next leap year is:"+str(n+a))






