from course_running import CourseRunning

class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
        self.running = []

    def add_running(self, year):
        cr = CourseRunning(self, year)
        self.running.append(cr)