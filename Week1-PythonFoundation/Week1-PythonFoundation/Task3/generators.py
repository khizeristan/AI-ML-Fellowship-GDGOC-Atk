# generators.py

# Fibonacci generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Custom range generator
def custom_range(start, end, step=1):
    current = start
    while current < end:
        yield current
        current += step

# Example usage
if __name__ == "__main__":
    print("Fibonacci sequence (10 numbers):")
    for num in fibonacci(10):
        print(num, end=" ")
    print("\n\nCustom range from 5 to 20 step 3:")
    for i in custom_range(5, 20, 3):
        print(i, end=" ")
