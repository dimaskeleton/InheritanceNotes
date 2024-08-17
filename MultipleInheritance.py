from typing import List

class Person:
    # Contract: Initializes a new instance of Person.
    # purpose: name (str), age (int)
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_age_info(self) -> str:
        return f"Name: {self.name}, Age: {self.age}"

class Employee:
    # purpose: Represents an employee with an ID and department information.
    # employee_id (str), department (str)

    def __init__(self, employee_id: str, department: str) -> None:
        self.employee_id = employee_id
        self.department = department

    def get_employee_details(self) -> str:
        return f"Employee ID: {self.employee_id}, Department: {self.department}"

# Purpose: Represents a teacher, inheriting attributes from both Person and Employee,
# and also includes subjects taught by the teacher.
# Contract: subjects_taught (List[str])

class Teacher(Person, Employee):
    def __init__(self, name: str, age: int, employee_id: str, department: str, subjects_taught: List[str]) -> None:
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, department)
        self.subjects_taught = subjects_taught

    def get_teacher_info(self) -> str:
        personal_info = self.get_personal_info()
        employee_details = self.get_employee_details()
        subjects = ", ".join(self.subjects_taught)
        return f"{personal_info}, {employee_details}, Subjects Taught: {subjects}"

#teacher = Teacher(name="Shajina Anand", age=34, employee_id="T1001", department="CSC", subjects_taught=["Cybersecurity", "Assembly", "OS"])
#print(teacher.get_teacher_info())






def test_person_initialization():
    person = Person("John Doe", 30)
    assert person.name == "John Doe"
    assert person.age == 30

def test_employee_initialization():
    employee = Employee("E1234", "HR")
    assert employee.employee_id == "E1234"
    assert employee.department == "HR"

def test_teacher_initialization():
    teacher = Teacher("Katie Smith", 35, "T1001", "Mathematics", ["Algebra", "Calculus", "Geometry"])
    assert teacher.name == "Katie Smith"
    assert teacher.age == 35
    assert teacher.employee_id == "T1001"
    assert teacher.department == "Mathematics"
    assert teacher.subjects_taught == ["Algebra", "Calculus", "Geometry"]

def test_get_personal_info():
    person = Person("John Doe", 30)
    assert person.get_personal_info() == "Name: John Doe, Age: 30"

def test_get_employee_details():
    employee = Employee("E1234", "HR")
    assert employee.get_employee_details() == "Employee ID: E1234, Department: HR"

def test_get_teacher_info():
    teacher = Teacher("Abdul Kalam", 75, "T1001", "Aero", ["Aerospace", "Calculus", "Geometry"])
    expected_info = "Name: Abdul Kalam, Age: 75, Employee ID: T1001, Department: Aero, Subjects Taught: Aerospace, Calculus, Geometry"
    assert teacher.get_teacher_info() == expected_info