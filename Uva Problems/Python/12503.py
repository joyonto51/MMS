T = int(input())
for k in range(T):
    N = int(input())
    List = []

    a = 0
    for j in range(N):
        IN = str(input())

        if IN == "RIGHT":
            a += 1
            List.append(IN)

        elif IN == "LEFT":
            a -=1
            List.append(IN)

        elif "SAME AS" in IN:
            b = int(IN[8:])-1

            if List[b]=="RIGHT":
                 a += 1
                 List.append("RIGHT")
            elif List[b]=="LEFT":
                 a -= 1
                 List.append("LEFT")

    print("{}".format(a))
