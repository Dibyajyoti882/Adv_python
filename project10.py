class StudentNotFound(Exception):
    pass


class InvalidGrade(Exception):
    pass


class GradeSystem:

    def __init__(self):
        self.students = {}

    def add_student(self, sid, grade):
        try:
            if grade == "":
                raise InvalidGrade("Grade cannot be empty")

            grade = int(grade)
            self.students[sid] = grade
            print("Student added successfully")

        except ValueError:
            print("Grade must be a number")

        except InvalidGrade as e:
            print(e)

    def update_grade(self, sid, grade):
        try:
            if sid not in self.students:
                raise StudentNotFound("Student ID not found")

            grade = int(grade)
            self.students[sid] = grade
            print("Grade updated")

        except ValueError:
            print("Invalid grade type")

        except StudentNotFound as e:
            print(e)

    def delete_student(self, sid):
        try:
            if sid not in self.students:
                raise StudentNotFound("Student ID not found")

            del self.students[sid]
            print("Student deleted")

        except StudentNotFound as e:
            print(e)

    def display(self):
        print("Student Grades:")
        for i in self.students:
            print(i, ":", self.students[i])



g = GradeSystem()

g.add_student("101", "85")
g.add_student("102", "90")

g.update_grade("101", "88")

g.delete_student("105")  

g.display()