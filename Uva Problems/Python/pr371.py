from time import clock
from Permit import *
@Permission
def main_func():
        L,H = map(int,input().split())
        while L==0 and H==0:
            break
        V = 0
        S = 0
        for x in range(L,H+1):
            y = x
            Z = 0
            while True:
                if x%2==0:
                    x = int(x/2)
                else:
                    x = int(3*x+1)
                Z+=1
                if x==1:
                    break

            if S < Z:
                S = Z
                V = y

        print("Between {} and {}, {} generates the longest sequence of {} values.".format(L,H,V,S))
        print("\n",clock())
