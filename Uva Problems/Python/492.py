from string import ascii_letters

while True:
    try:
        s = str(input())
    except:
        break
    B = ascii_letters
    C = 'AEIOUaeiou'
    S,s2,s3 ="","",""

    for j in range(len(s)):
        if s[j] in B:
            m = 1
        else:
            m = 0
        if m == 1:
            s2 += s[j]
        else:
            s3 += s[j]

        if m == 0 and s2 != "":
            if len(s2)==1 or s2[0] in C:
                s2+="ay"
                S+=s2
                s2=""
            elif s2[0] in B:
                d=s2[0]
                s2=s2[1:]+d+"ay"
                S+=s2
                s2 = ""
        elif m == 1 and s3 != "":
            S+=s3
            s3 = ""
        m1=m
    if m1==1 and s2!="":
        if len(s2)==1 or s2[0] in C:
                s2+="ay"
                S+=s2

        elif s2[0] in B:
            d=s2[0]
            s2=s2[1:]+d+"ay"
            S+=s2
    else:
        S+=s3

    print(S)
