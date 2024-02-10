class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

class Student(Person):
    def __init__(self, name, surname, age, university):
        super().__init__(name, surname, age)
        self.university = university

    @property
    def attributes(self):
        return f"name: {self.name}, surname: {self.surname}, age: {self.age}"


