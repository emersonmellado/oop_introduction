from basics.person_3 import Person

class Program:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
    def details(self):
        print("Course name:", self.name, "Duration:",self.duration)

n = input("Enter the program name")
d = input("Enter the program duration")
course_1 = Program(n, d)
course_1.details()

student = Person("John Rambo", 33, "DevOps", "Master")