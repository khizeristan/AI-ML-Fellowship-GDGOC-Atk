# utils.py

def greet_user(Khizer):
    """Return a greeting message."""
    return f"Hello, {Khizer}!"

def multiply(*args):
    """Multiply all numbers passed as arguments."""
    result = 1
    for num in args:
        result *= num
    return result

def print_dict(d):
    """Print dictionary in readable format."""
    for key, value in d.items():
        print(f"{key}: {value}")

# Lambda example
square = lambda x: x ** 2
