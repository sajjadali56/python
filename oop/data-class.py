from dataclasses import dataclass


@dataclass
class Person:
    """A simple person class."""
    name: str
    age: int

    def __str__(self):
        return f"{self.name} is {self.age} years old"


person = Person("John", 30)
print(person)
