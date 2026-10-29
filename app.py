def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def is_even(number):
    """Return True if the number is even."""
    return number % 2 == 0


def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("TrustLens"))
    print("Sum:", add_numbers(10, 20))
    print("Is 8 even?", is_even(8))
