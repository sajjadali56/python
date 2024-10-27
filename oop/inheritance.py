class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent constructor to initialize 'species'
        super().__init__(species="Dog")
        self.name = name
        self.breed = breed

    def speak(self):
        print("Woof! Woof!")

# Creating an instance of Dog
dog = Dog(name="Buddy", breed="Golden Retriever")
print(dog.species)  # Output: Dog
dog.speak()         # Output: Woof! Woof!


"""
In multiple inheritance, super() can be used to call the constructors 
of multiple parent classes in the order specified by the Method Resolution Order (MRO).
"""
class A:
    def __init__(self):
        print("A's constructor")
        super().__init__()  # Calls the next constructor in MRO

class B:
    def __init__(self):
        print("B's constructor")

class C(A, B):
    def __init__(self):
        print("C's constructor")
        super().__init__()  # Calls B's constructor, then A's constructor due to MRO

c = C()
# Output:
# C's constructor
# B's constructor
# A's constructor


"""
In some cases, you may want to call a specific parent’s constructor directly (e.g., A.__init__(self)). 
This bypasses super() and can be used when you need direct control over which parent constructor is invoked.
"""

# class X:
#     def __init__(self):
#         print("X's constructor")

# class Y:
#     def __init__(self):
#         print("Y's constructor")

# class Z(X, Y):
#     def __init__(self):
#         print("Z's constructor")
#         X.__init__(self)  # Direct call to X's constructor
#         Y.__init__(self)  # Direct call to Y's constructor

# z = Z()
# Output:
# Z's constructor
# X's constructor
# Y's constructor
