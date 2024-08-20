import time

def time_it(func):
  """
    Decorator to measure the execution time of a function.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The decorated function with execution time measurement.

    Example:
        >>> @time_it
        ... def example_func():
        ...     time.sleep(1)
        >>> example_func()
        Function 'example_func' took 1000.000 µs to execute.
    """

  def wrapper(*args, **kwargs):
    
    start_time = time.perf_counter()  # Use high-resolution timer
    
    result = func(*args, **kwargs)
    
    end_time = time.perf_counter()
    
    elapsed_time = end_time - start_time
    
    print(f"Function '{func.__name__}' took {elapsed_time*10**6:.3f} µs to execute.")
    
    return result

  return wrapper

def alphaNum(char):
  """
  Returns True if the input character is alphanumeric, False otherwise.

  Args:
    c (str): The input character to check.

  Returns:
    bool: True if the input character is alphanumeric, False otherwise.
  """
  return (ord('A') <= ord(char) <= ord('Z') or 
                ord('a') <= ord(char) <= ord('z') or 
                ord('0') <= ord(char) <= ord('9'))