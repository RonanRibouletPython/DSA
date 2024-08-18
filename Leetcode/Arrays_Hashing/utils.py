import time

def time_it(func):
  """Decorator to measure the execution time of a function."""

  def wrapper(*args, **kwargs):
      
    start_time = time.perf_counter()  # Use high-resolution timer
    
    result = func(*args, **kwargs)
    
    end_time = time.perf_counter()
    
    elapsed_time = end_time - start_time
    
    print(f"Function '{func.__name__}' took {elapsed_time*10**6:.3f} µs to execute.")
    
    return result

  return wrapper