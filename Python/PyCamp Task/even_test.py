# coding=utf-8
def odd_even_test(num):
    if num%2==0:
        return True
    else:
        return False

def test_odd_even():
    assert odd_even_test(6)== True
def test_odd():
    assert odd_even_test(5)== False