# Task 2: A Decorator that takes an Argument
def type_converter(type_of_input):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return type_of_input(func(*args, **kwargs))
        return wrapper
    return decorator

@type_converter
def return_int():
    return 5

@type_converter
def return_string():
    return "not a number"

if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__) # This should print "str"

    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!") # This is what should happen