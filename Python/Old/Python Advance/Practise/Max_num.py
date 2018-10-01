List=list(map(int,input().split()))
max=List[0]
index = 0

for i in range(1,len(List)):
    if List[i]>max:
        max=List[i]
        index=i

print("Max_num =",max,", index = ",index)
