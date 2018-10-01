var1 = 0
var2 = 1
n = int(input("Enter a number:"))
for i in range(n+1):
    print(var2)
    var3 = var1 + var2
    var1 = var2
    var2 = var3
