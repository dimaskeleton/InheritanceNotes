from typing import Any

# Purpose: class with a person with basic information.
# Contract: Initializes with name (str) and age (int), and a method to display these attributes

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def display(self) -> None:
        print(f"Name: {self.name}, Age: {self.age}")

# Purpose: Extend Person to model a student with a student ID and major.
# Contract: Inherits name and age from Person and adds student_id (str) and major (str)
# with an enhanced display method

class Student(Person):
    def __init__(self, name: str, age: int, student_id: str, major: str) -> None:
        super().__init__(name, age)  # Call the constructor of the parent class
        self.student_id = student_id
        self.major = major

    def display(self) -> None:
        # Overriding the display method to include student-specific details
        super().display()  # Call the display method of the parent class
        print(f"Student ID: {self.student_id}, Major: {self.major}")












def test_person_init():
    # Purpose: Ensure that the Person object is correctly initialized with the name and age attributes.
    # Contract: The Person object should store the name and age passed to its constructor.

    name = "Twinkle"
    age = 9
    person = Person(name, age)
    assert person.name == name
    assert person.age == age

def test_student_init():
    # Purpose: Ensure that the Student object inherits attributes from Person and initializes its own attributes correctly.
    # Contract: The Student object should store the name, age, student_id, and major passed to its constructor.

    name = "Rianna"
    age = 10
    student_id = "CS23456"
    major = "Computer Science"

    student = Student(name, age, student_id, major)
    assert student.name == name
    assert student.age == age
    assert student.student_id == student_id
    assert student.major == major

def test_person_display(capsys):
    # Purpose: Verify that the display method of the Person class outputs the correct information.
    # Contract: The output should match the expected format "Name: <name>, Age: <age>\n"

    person = Person("Twinkle", 10)
    person.display()
    captured = capsys.readouterr()  # Capture the output of the display method
    assert captured.out == "Name: Twinkle, Age: 10\n", "The output of Person.display() should match the expected format."