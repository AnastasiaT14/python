from abc import ABC, abstractmethod

class AverageNumCalcMixin:
    def calculate_average(self, values):
        if not values:
            return 0

        total = sum(values)
        num_values = len(values)
        return total / num_values if num_values > 0 else 0

class Person(ABC):
    def __init__(self, student_id, name):
        self._student_id = student_id
        self.name = name

    @abstractmethod
    def display_details(self):
        pass

class Student(Person, AverageNumCalcMixin):
    def __init__(self, student_id, name):
        super().__init__(student_id, name)
        self.grades = {}

    def add_grades(self, subject, grades):
        self.grades[subject] = grades

    def average_grades(self):
        # Flatten the list of grades for all subjects
        all_grades = [grade for subject_grades in self.grades.values() for grade in subject_grades]
        return self.calculate_average(all_grades)

    def display_details(self):
        avg_grade = self.average_grades()
        print(f"Student ID: {self._student_id} Name: {self.name} Average grade: {avg_grade:.2f}")

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        new_student = Student(student_id, name)
        self.students[student_id] = new_student

    def show_student_details(self, student_id):
        if student_id in self.students:
            return self.students[student_id].display_details()
        else:
            return "Student not found."

    def show_student_average_grade(self, student_id):
        if student_id in self.students:
            return self.students[student_id].average_grades()
        else:
            return "Student not found."



sms = StudentManagementSystem()
sms.add_student(1, "Max")
sms.students[1].add_grades("Math", [80, 90, 75])
sms.students[1].add_grades("English", [95, 85, 90])
print(sms.show_student_details(1))
print(sms.show_student_average_grade(1))
sms.add_student(2, "Nia")
print(sms.show_student_details(2))
sms.students[2].add_grades("Math", [70, 80, 90])
sms.students[2].add_grades("English", [80, 90, 85])
print(sms.show_student_details(2))
print(sms.show_student_average_grade(2))