
class Program:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

course_1 = Program("DevOps", "100 hours")

def details(course):
    print("Course name:", course.name, "Duration:",course.duration)

details(course_1)

