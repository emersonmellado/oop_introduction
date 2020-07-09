class Student:
    def __init__(self, name, student_number):
        self.name = name
        self.student_number = student_number
        self.courses = []
    def enrol(self, course):
        for r in course.running:
            if (r.year != 2020):
                print("This course", course.name, "is not running, therefore it cannot be assigned")
                return
        self.courses.append(course)