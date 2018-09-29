def Permission(func):
    while True:
        func()
        while True:
                T = str(input("\nTo continue press 'Y' or press 'N' to stop :"))
                if (T=="Y") or (T=="y"):
                        break
                elif (T=="N") or (T=="n"):
                    break
                else:
                    print("Wrong input!")


        if (T=="N") or (T=="n"):
                    break

