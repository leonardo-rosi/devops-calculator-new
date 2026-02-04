from operations import sum

def test_sum_integer_numbers():
    assert sum(2, 3) == 5
    assert sum(-1, 1) == 0
    assert sum(0, 0) == 0

def test_sum_float_numbers():
    assert sum(2.5, 3.5) == 6.0
    assert sum(-1.0, 1.0) == 0.0
    assert sum(0.0, 0.0) == 0.0

def test_stings_inputs():
    assert sum("hello", 5) is None
    assert sum(5, "world") is None
    assert sum("hello", "world") is None

def test_sum_zeroes():
    assert sum(0, 5) == 5
    assert sum(5, 0) == 5
    assert sum(0, 0) == 0


