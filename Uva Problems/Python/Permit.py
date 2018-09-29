def Permission(func):
        while True:
            func()
            while True:
                T = str(input("To continue press 'Y' or press 'N' to stop :"))

                if (T=="Y") or (T=="y"):
                    break
                if (T=="N") or (T=="n"):
                    break
                else:
                    continue
            if (T=="N") or (T=="n"):
                break
