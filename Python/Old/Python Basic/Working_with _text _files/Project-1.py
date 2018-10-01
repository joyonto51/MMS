def add():
    name=input("Enter the name of student:")
    addr=input("Enter the address:")
    data="{:15s}{:30s}".format(name,addr)
    file=open("data.txt","a")
    file.write(name + "\n")
    file.write(addr + "\n")
    file.write("----------------------------------------"+"\n")
    file.close

add()
file=open("data.txt","r")
print(file.read())


