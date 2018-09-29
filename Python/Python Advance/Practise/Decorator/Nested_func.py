
def parent(num):

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    try:
        assert num == 5
        return first_child()
    except AssertionError:
        return second_child()

foo = parent(5)
bar = parent(6)

print(type(foo))
print(bar)