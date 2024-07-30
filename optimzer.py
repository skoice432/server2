import time
import functools
import concurrent.futures

def timer_decorator(func):
    """Decorator to measure execution time"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

def cache_decorator(func):
    """Decorator to cache function results"""
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

@timer_decorator
@cache_decorator
def fibonacci(n):
    """Calculate Fibonacci number"""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def parallel_fibonacci(n):
    """Calculate Fibonacci number using parallel processing"""
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(fibonacci, n)
        return future.result()

if __name__ == "__main__":
    n = 30
    print(f"Fibonacci number {n}: {parallel_fibonacci(n)}")