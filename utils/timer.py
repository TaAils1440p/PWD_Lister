import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"🕒 Starting {func.__name__}...")
        result = func(*args, **kwargs)
        end = time.time()
        print(f"✅ Completed in {end - start:.2f} seconds.")
        return result
    return wrapper
