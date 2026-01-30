# exception_handling.py

def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except TypeError:
        print("Error: Invalid input type!")
        return None
    else:
        print("Division successful!")
    finally:
        print("Operation completed.")

# Example usage
if __name__ == "__main__":
    print(safe_division(10, 2))
    print(safe_division(10, 0))
    print(safe_division(10, "a"))
