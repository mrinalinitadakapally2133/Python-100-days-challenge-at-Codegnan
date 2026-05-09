from calculator import add, division


# test addition function
def test_add1():
    assert add(5,6) == 11

def tes_add2():
    assert add(5,5) == 10

# twst division function
def test_div1():
    assert division(10,2) == 5.0
def test_div2():
    assert division(10,2) == 5.1