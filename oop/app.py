class Student:
    college_name = "SIBA" # Class Attr -> Can be access as Student.college_name

    def __init__(self):
        print("Default Constructor")

    def __init__(self, name, marks):
        # Class (Object) Attributes
        self.name = name 
        self.marks = marks

    def welcome(self):
        print("Hello", self.name)

    def avg_marks(self):
        sum = 0
        for marks in self.marks:
            sum += marks
        return sum / len(self.marks)

    def get_marks(self):
        return self.marks

    @property
    def percent(self):
        return str(self.avg_marks()) + "%"
    
    @staticmethod
    def hey():
        print("hey there")

    @classmethod
    def colleg(cls):
        return cls.college_name

Student.hey()
std = Student("Ali", [78, 56, 67])
# print(std.name, std.college_name)
print(std.name, std.percent)


"""
std.college_name = "KIBA" creates an instance variable college_name specifically for std. 
This does not change the class variable college_name; it only overrides it for std.
"""
std.college_name = "KIBA"
std.grade = "A"

s2 = Student("Sajjad Ali", 98)
print(s2.name, s2.college_name, std.college_name)

std.welcome()

class LawStudent(Student):

    def __init__(self):
        print("Child Constructor")


print()
std = LawStudent() # Child Constructor