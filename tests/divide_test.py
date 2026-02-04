from operations import divide

def test_divide_integer_numbers():
    assert divide(6, 3) == 2
    assert divide(-4, 2) == -2
    assert divide(0, 5) == 0

def test_divide_float_numbers():
    assert divide(7.5, 2.5) == 3.0
    assert divide(-4.0, 2.0) == -2.0
    assert divide(0.0, 5.0) == 0.0

def test_divide_string_inputs():
    assert divide("hello", 5) is None
    assert divide(5, "world") is None
    assert divide("hello", "world") is None

def test_divide_by_zero():
    assert divide(5, 0) is None
    assert divide(0, 0) is None
    assert divide(-3, 0) is None

def test_divide_one():
    assert divide(7, 1) == 7
    assert divide(1, 7) == 1/7
    assert divide(3.5, 1.0) == 3.5
    assert divide(1.0, 3.5) == 1.0/3.5

