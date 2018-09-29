List=list(map(int,input().split()))
print("PERFECTION OUTPUT")
for item in List:
    S=0
    a = (item//2)+1
    for i in range(1,a):
        if item==0:
            break
        elif int(item%i)==0:
            S+=i
    if item!=0:
        if item==S:
            print("%5d  PERFECT"%(item))
        elif item<S:
            print("%5d  ABUNDANT"%(item))
        else:
            print("%5d  DEFICIENT"%(item))

    else:
        print("END OF OUTPUT")
        break
