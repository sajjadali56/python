from datetime import date

class Employee:
    def __init__(self, name: str, birth_date: str):
        self.name: str = name
        self.birth_date: date = birth_date

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value.upper()
 

    @property
    def birth_date(self) -> date:
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value: str):
        self._birth_date = date.fromisoformat(value)


john = Employee("John", "2001-02-07")

print(john.name) # 'JOHN'

print(john.birth_date) # datetime.date(2001, 2, 7)


john.name = "John Doe"
print(john.name) #'JOHN DOE'