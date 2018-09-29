T = int(input())
for i in range(T):
    N = int(input())
    all_num = ""
    for i in range(1,N+1):
        all_num += str(i)

    a = int(all_num.count('0'))
    b = int(all_num.count('1'))
    c = int(all_num.count('2'))
    d = int(all_num.count('3'))
    e = int(all_num.count('4'))
    f = int(all_num.count('5'))
    g = int(all_num.count('6'))
    h = int(all_num.count('7'))
    i = int(all_num.count('8'))
    j = int(all_num.count('9'))

    print("{} {} {} {} {} {} {} {} {} {}".format(a,b,c,d,e,f,g,h,i,j))
