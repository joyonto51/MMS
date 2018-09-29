#A = "Iaamastudent"
#B=[A[i:i+2] for i in range(0,len(A),2)]
# C='abcdefghijklmnopqrstuvwxyz'
# Dict={}
# a = 97
# for i in range(len(C)):
#     Dict.update({C[i]:a})
#     a+=1
# print(Dict)
A=list(map(int,input().split()))
B=[]
a=0
for item in A:
    a+=item
    B.append(a)
print(B)
