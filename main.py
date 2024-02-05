class Student:
    university = "Hogwarts"

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __str__(self):
        return "Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    @property
    def is_passing(self):
        return int(self.grade) > 60

    def increase_grade(self, increase):
        self.grade = str(int(self.grade) + increase)


student = Student("Mari", 60, 20)
print(str(student))
print("Is passing:", student.is_passing)
student.increase_grade(10)

