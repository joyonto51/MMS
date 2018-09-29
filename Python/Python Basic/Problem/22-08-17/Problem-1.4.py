 inp=input("Enter the value of Arm1:")
arm1=int(inp)
inp=input("Enter the value of Arm2:")
arm2=int(inp)
inp=input("Enter the value of Arm3:")
arm3=int(inp)

if arm1+arm2>arm3 and arm2+arm3>arm1 and arm1+arm3>arm2:
    print("The Triangle is possible")
else:
    print("The Triangle is not Possible")
