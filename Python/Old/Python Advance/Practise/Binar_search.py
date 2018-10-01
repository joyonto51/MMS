Arr = [1,2,4,5,6,8,9,11,13,15,17]
c = int(input())
m = 0
begin = 1
end = len(Arr)
mid = (begin + end) // 2
while(begin<=end) and (Arr[mid] != c):
    if c < Arr[mid]:
        end = mid-1
    else:
        begin = mid+1

    mid = (begin+end)//2

    if Arr[mid]==c:
        m = mid+1
        break
    else:
        m = -1

print(m)