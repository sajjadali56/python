def requires_login(func):
    def wrapper(self, *args, **kwargs):
        if not self.logged_in:
            print("Please log in first.")
            return
        return func(self, *args, **kwargs)
    return wrapper

class User:
    def __init__(self, name):
        self.name = name
        self.logged_in = False

    @requires_login
    def view_dashboard(self):
        print(f"Welcome to your dashboard, {self.name}.")

user = User("Alice")
user.view_dashboard()  # Output: Please log in first.
user.logged_in = True
user.view_dashboard()  # Output: Welcome to your dashboard, Alice.


class Person:
    def __init__(self, name):
        self._name = name  # Protected attribute (by convention)

    @property
    def name(self):
        # Getter method
        print("Getting name")
        return self._name

    @name.setter
    def name(self, value):
        # Setter method
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        print("Setting name")
        self._name = value

# Usage
person = Person("Alice")
print(person.name)   # Calls the getter -> Output: Getting name \n Alice
person.name = "Bob"  # Calls the setter -> Output: Setting name
print(person.name)   # Output: Getting name \n Bob


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        # Computed property, no setter needed
        return self._width * self._height

# Usage
rect = Rectangle(5, 10)
print("Area", rect.area)  # Output: 50 (computed based on width and height)
