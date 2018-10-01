x =[i*2 for i in range(10)]

print(x)

y = [[i for i in range(5)], [i*2 for i in range(5,10)], [['Bangladesh','India']]]
print(y)

if [i for i in y if 'India' in i]:
    print('yes')

z = ['1','2','3','4','5']
z1 = [int(i) for i in z]
print(z1)

vec = [[1,2,3], [4,5,6], [7,8,9]]
D = [i for z in vec for i in z]

[print(x) for x in D]