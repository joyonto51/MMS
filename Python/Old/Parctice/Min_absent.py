test_list = [1,2,3,4,5,6,8]
min_absent = 0

n = max(test_list)
for i in range(1, n):
    if i not in test_list:
        min_absent = i
        break

print(min_absent)