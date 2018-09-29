a_list=['name', 'country','career']
b_list=['Teletalk','Bangladesh','Jayanta ']
my_dict={i:j for i,j in zip(a_list,b_list)}
print(my_dict)
new_dict={key:value for value,key in my_dict.items()}
print(new_dict)

def add(*args):
    tmp=0
    for number in args:
        tmp=tmp+number

    return tmp

temp=add(1,3,4,56,7,8)
print(temp)
print(type(temp))

