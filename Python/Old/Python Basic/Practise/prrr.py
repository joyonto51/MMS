n=int(input())
if(n==1):
    a=int(input("Enter an hour:"))
    b=int(input("Enter another hour:"))
    if(a<=b):
      B=b-a
      print(str(B),"hour")
    elif(a>b):
       A=(12-a)+b
       print(str(A),"hour")
    else:
       print("Error")
elif(n==2):
    s=int(input())
    i=0
    for i in range(0,s,-1):
        print(i)




