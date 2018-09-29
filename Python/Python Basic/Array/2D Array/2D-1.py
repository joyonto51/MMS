list = []
for i in range(5,5):
    s=""

    for j in range(i,4):
        s+="  "
    for k in range(1,i*2):
        s+='* '

    list.append(s)


for item in list:
    print(item,"\n")
