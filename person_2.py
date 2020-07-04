class Person:
    def __init__(self, name, age, program, role):  # this is the constructor
        self.name = name
        self.age = age
        self.program = program
        self.role = role
    def say_hello(self):
        print("Hello :) My name is", self.name, "I am", self.age, "years old, enrolled in", self.program, "and my role is", self.role)

student_1 = Person("John", 37, "DevOps Course", "Student")
student_1.say_hello()

student_2 = Person("Mary", 22, "DevOps Course", "Student")
student_2.say_hello()

coordinator_1 = Person("Jane", 34, "DevOps Course", "Coordinator")
coordinator_1.say_hello()

instructor_1 = Person("Bruce", 35, "DevOps Course", "Instructor")
instructor_1.say_hello()