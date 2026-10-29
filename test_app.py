from app import add_numbers, is_even, greet


def test_add_numbers():
    assert add_numbers(10, 20) == 30
    assert add_numbers(-1, 1) == 0


def test_is_even():
    assert is_even(8) is True
    assert is_even(7) is False


def test_greet():
    assert greet("TrustLens") == "Hello, TrustLens!"
