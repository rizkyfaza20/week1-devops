from calculator import add, div, mul, sub

def test_add():
    assert add(2, 3) == 9

def test_sub():
    assert sub(2, 3) == -1

def test_mul():
    assert mul(2, 3) == 6

def test_div():
    assert div(2, 3) == 0.6666666666666666