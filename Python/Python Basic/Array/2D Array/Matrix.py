# coding=utf-8
x = int(input("Enter the number of row:"))
y = int(input("Enter the number of colum:"))
list=[]
print("Enter the matrix elements:")
for i in range(x*y):
    m = int(input())
    list.append(m)
List=[]
ln = 0
for i in range(0,len(list),y):
    list2=[]
    for j in range(i,i+y):
        d = str(list[j])
        if ln<len(d):
            ln=len(d)
        list2.append(d)
    List.append(list2)

print("\n\n")
print("The Matrix\n-----------")
for k in range(len(List)):
    a = List[k]
    b = ".join(a)
    print(b)


