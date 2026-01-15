# Task 1: Writing and Testing Decorator

# one time setup
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

# To write a log record:
logger.log(logging.INFO, "this string would be logged")

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        # log a message saying which function was called, and what arguments it got
        logger.info(f"calling_function'{func.__name__} with args={args} kwargs={kwargs}")
        # log a message saying what the function returned
        logger.info(f"calling_function'{func.__name__} returned {result}")
        return result
    return wrapper

@logger_decorator
def greeting():
    print("Hello, World!")

@logger_decorator
def return_true(a, *b):
    if a + sum(b) > 0:
        return True
    
@logger_decorator
def return_log_dec(**kwargs):
    return kwargs

if __name__ == "__main__":
    greeting()
    print(return_true(2, 3, 4))
    print(return_log_dec(name="Belle", state="California"))




    
    