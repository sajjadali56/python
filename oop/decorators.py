def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()

# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.



def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Output:
# Before the function call
# Hello, Alice!
# After the function call




def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)  # Capture return value
        print("After the function call")
        return result  # Return result to caller
    return wrapper

@my_decorator
def add(x, y):
    return x + y

result = add(3, 4)
print("Result:", result)

# Output:
# Before the function call
# After the function call
# Result: 7




def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def greet_decorator(func):
    def wrapper(*args, **kwargs):
        print("Hello!")
        return func(*args, **kwargs)
    return wrapper

@greet_decorator
@uppercase
def greet(name):
    return f"Good morning, {name}"

print(greet("Alice"))

# Output:
# Hello!
# GOOD MORNING, ALICE
