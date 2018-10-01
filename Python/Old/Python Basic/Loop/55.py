x=int(input("Please enter obtain marks:"))

if(x<40):
    print("The result is : 'Fail'")
elif(x>=40 and x<=49):
    print("The result is : 'D'")
elif(x>=50 and x<=59):
    print("The result is : 'C'")
elif(x>=60 and x<=69):
    print("The result is : 'B'")
elif(x>=70 and x<=79):
    print("The result is : 'A'")
elif(x>=80 and x<=100):
    print("The result is : 'A+'")
else:
    print("Error")
