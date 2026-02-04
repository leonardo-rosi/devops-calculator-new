from operations import multiply

def test_multiply_integer_numbers():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0

def test_multiply_float_numbers():
    assert multiply(2.5, 4.0) == 10.0
    assert multiply(-1.0, 1.0) == -1.0
    assert multiply(0.0, 5.5) == 0.0

def test_multiply_string_inputs():
    assert multiply("hello", 5) is None
    assert multiply(5, "world") is None
    assert multiply("hello", "world") is None

def test_multiply_zero():
    assert multiply(0, 100) == 0
    assert multiply(100, 0) == 0
    assert multiply(0, 0) == 0

def test_multply_one():
    assert multiply(1, 7) == 7
    assert multiply(7, 1) == 7
    assert multiply(1.0, 3.5) == 3.5
    assert multiply(3.5, 1.0) == 3.5

