T = int(input())
for i in range(T):
    N = int(input())
    a,b,c,d,e,f,g,h,i,j=0,0,0,0,0,0,0,0,0,0

    for n in range(1,N+1):
        while n!=0:
            m = n%10
            n = n//10
            if m==0:
                a+=1
            elif m==1:
                b+=1
            elif m==2:
                c+=1
            elif m==3:
                d+=1
            elif m==4:
                e+=1
            elif m==5:
                f+=1
            elif m==6:
                g+=1
            elif m==7:
                h+=1
            elif m==8:
                i+=1
            else:
                j+=1

    print(a,b,c,d,e,f,g,h,i,j)
0.0.
