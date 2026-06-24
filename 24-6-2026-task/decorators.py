import time
import logging
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"STARTED : {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"COMPLETED : {func.__name__}")
        return result
    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logging.info(
            f"{func.__name__} executed in "
            f"{end-start:.2f} seconds"
        )
        return result
    return wrapper