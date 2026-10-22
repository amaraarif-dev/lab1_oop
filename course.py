
class InvalidMarksError(Exception):
    pass


class Course:
    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_student(self, student, marks):
        if marks < 0 or marks > 100:
            raise InvalidMarksError(
                f"Invalid marks for {student}: {marks}"
            )

        self.marks[student] = marks

    def average(self):
        if len(self.marks) == 0:
            return 0.0

        return sum(self.marks.values()) / len(self.marks)

    def top_student(self):
        if len(self.marks) == 0:
            return None

        return max(self.marks, key=self.marks.get)

    def __len__(self):
        return len(self.marks)

    def __str__(self):
        count = len(self.marks)
        word = "student" if count == 1 else "students"

        return (
            f"{self.name}: {count} {word}, "
            f"average {self.average():.1f}"
        )

    # Bonus B1: Remove a student
    def remove_student(self, name):
        if name not in self.marks:
            raise KeyError(f"No student named {name}")

        del self.marks[name]

    # Bonus B2: Save a report
    def save_report(self, filename):
        with open(filename, "w") as file:
            for name, marks in self.marks.items():
                status = "Pass" if marks >= 50 else "Fail"
                file.write(f"{name}: {marks} ({status})\n")

            file.write(f"Average: {self.average():.1f}\n")

    # Bonus B3: Combine two courses
    def __add__(self, other):
        new_course = Course(self.name + " + " + other.name)

        for name, marks in self.marks.items():
            new_course.add_student(name, marks)

        for name, marks in other.marks.items():
            new_course.add_student(name, marks)

        return new_course
    


def load_course(name, filename):
    course = Course(name)

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                try:
                    student, mark = line.split(",", 1)
                    student = student.strip()
                    mark = int(mark.strip())

                    course.add_student(student, mark)

                except ValueError:
                    print(f"Skipping {line.split(',')[0]}: marks is not a number")

                except InvalidMarksError as error:
                    print(f"Skipping: {error}")

    except FileNotFoundError:
        print(f"File not found: {filename}")

    return course


# Run this file directly to test the Course class
if __name__ == "__main__":
    test = Course("Test")
    test.add_student("A", 50)
    print(test)
def remove_student(self, name: str) -> None:
    """Remove a student, or raise KeyError if missing."""
    if name not in self.marks:
        raise KeyError(f"No student named {name}")
    del self.marks[name]