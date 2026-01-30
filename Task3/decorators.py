# decorators.py
import time

def execution_time(func):
    """Custom decorator to measure function execution time"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time of {func.__name__}: {end - start:.6f} seconds")
        return result
    return wrapper

# Example usage
@execution_time
def sample_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

if __name__ == "__main__":
    print(sample_function(100000))
