from calculator import add_fun, sub_fun

def test_add():
    assert add_fun(1, 3) == 4

def test_sub():
    assert sub_fun(4, 1) == 3