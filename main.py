from course import Course, InvalidMarksError, load_course


# Task 1: Student class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def passed(self):
        return self.marks >= 50

    def __str__(self):
        status = "Pass" if self.passed() else "Fail"
        return f"{self.name} ({self.marks}): {status}"


print("TASK 1: STUDENT CLASS")

students = [
    Student("Ali", 72),
    Student("Sara", 45),
    Student("Omar", 50)
]

for student in students:
    print(student)


# Task 2: Test Course class
print("\nTASK 2: COURSE CLASS")

c = Course("Programming for AI")

c.add_student("Ali", 88)
c.add_student("Sara", 92)
c.add_student("Omar", 75)

print(len(c))
print(c.average())
print(c.top_student())


# Task 3: Custom exception
print("\nTASK 3: CUSTOM EXCEPTION")

try:
    c.add_student("Bilal", 120)
except InvalidMarksError as error:
    print("Error:", error)

print(c)


# Task 4: Load students from marks.txt
print("\nTASK 4: LOAD FROM FILE")

course = load_course("Programming for AI", "marks.txt")

print(course)
print("Top student:", course.top_student())


# Test a missing file
print("\nTEST MISSING FILE")

load_course("Programming for AI", "mark.txt")


# Task 5: Modules
# Course class and load_course are imported from course.py.
# All course logic is maintained in course.py.


#s Remove a student
print("\nBONUS B1: REMOVE STUDENT")

try:
    course.remove_student("Zara")
except KeyError as error:
    print(error)


# Save report
print("\nBONUS B2: SAVE REPORT")

course.save_report("report.txt")
print("Report saved successfully.")


# Combine courses
print("\nBONUS B3: COMBINE COURSES")

second_course = Course("Python")
second_course.add_student("Ahmed", 80)

combined = course + second_course
print(combined)
print(combined.marks)
# AI Assistance Declaration
# I used ChatGPT to help me write and organize this assignment.
# I have reviewed the code and understand its logic, including
# classes, methods, exception handling, file handling, and imports.
# I can explain how the code works.