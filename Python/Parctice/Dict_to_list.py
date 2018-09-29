## Task 1
test_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

# Write your code here
test = []
for key, value in sorted(test_dict.items()):
    a = (key, value)
    test.append(a)

test_dict = test

print(test_dict)  # [('a', 1), ('b', 2), ('c',3), ('d',4)]