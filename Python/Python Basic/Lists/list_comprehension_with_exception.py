my_list = [1, 23, 45, 'hello', '43', -23, '-56', 'one', 5.6]
another_list = []

for item in my_list:
    try:
        another_list.append(int(item))

    except ValueError:
        pass
        #print("'{}' is not able to convert into integer".format(item))

print(another_list)

[print(item) for item in another_list]