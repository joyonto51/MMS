# coding=utf-8
from Des_func3 import my_decorator

@my_decorator
def just_some_function():
    print("Hurrah!")

just_some_function()