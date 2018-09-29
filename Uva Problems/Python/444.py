while True:
    try:
        I=str(input())
    except:
        break
    Dict={'x': 120, 'j': 106, 'l': 108, 'p': 112, 'd': 100, 'k': 107, 'r': 114, 't': 116, 'b': 98, 'a': 97, 'h': 104, 'z': 122, 'e': 101, 'c': 99, 's': 115, 'i': 105, 'o': 111, 'u': 117, 'g': 103, 'm': 109, 'w': 119, 'y': 121, 'n': 110, 'f': 102, 'v': 118, 'q': 113,'Y': 89, 'N': 78, 'V': 86, 'E': 69, 'A': 65, 'S': 83, 'J': 74, 'U': 85, 'D': 68, 'O': 79, 'C': 67, 'M': 77, 'R': 82, 'L': 76, 'H': 72, 'X': 88, 'F': 70, 'T': 84, 'Q': 81, 'I': 73, 'Z': 90, 'P': 80, 'K': 75, 'G': 71, 'B': 66, 'W': 87,' ': 32,'!': 33,',': 44,'.':46,':':58,';':59,'?':63}
    C="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!,.:;?"
    N="0123456789"
    S,list="",[]
    if len(I)!=0:
        if I[0] in C:
            for i in range(len(I)):
                item=I[i]
                for key,value in Dict.items():
                    if item==key:
                        S+=str(value)
            S=S[::-1]

        elif I[0] in N:
            I=I[::-1]
            j,k=0,2
            for i in range(0,len(I)-1,2):
                x=int(I[j:k])
                if 31<x and x<100:
                    list.append(x)
                else:
                    y=int(I[j:k+1])
                    list.append(y)
                    k+=1
                    j+=1
                if k+1>=len(I):
                    break
                k+=2
                j+=2

            for item in list:
                for key,value in Dict.items():
                    if int(item)==value:
                        S+=key
    else:
        print("")
        continue
    print(S)
