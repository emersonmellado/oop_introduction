from student import Student
from course import Course

joe = Student("Joe", 5)
mary = Student("Mary", 1)

course_1 = Course("DevOps", 35)
course_2 = Course("Python", 10)
course_1.add_running(2020)
course_2.add_running(2021)

print(vars(course_1), "year", course_1.running[0].year)
print(vars(course_2), "year", course_2.running[0].year)

joe.enrol(course_1)
joe.enrol(course_2)

print("Student=", vars(joe))
# print("Student=", vars(mary))
# print("Course=", vars(course_1))

"""
The structure of the object joe (Student) is the following
Students can participate on courses 
as long as the course is running.

Student
    Course
        CourseRunning
"""