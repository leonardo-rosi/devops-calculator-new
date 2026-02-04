from operations import subtract

def test_subtract_integer_numbers():
    assert subtract(5, 3) == 2
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0

def test_subtract_float_numbers():
    assert subtract(5.5, 2.5) == 3.0
    assert subtract(-1.0, 1.0) == -2.0
    assert subtract(0.0, 0.0) == 0.0

def test_subtract_string_inputs():
    assert subtract("hello", 5) is None
    assert subtract(5, "world") is None
    assert subtract("hello", "world") is None

def test_subtract_zero():
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5
    assert subtract(0, 0) == 0

