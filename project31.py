# Design a School Management System that includes classes for Student, Teacher, and Admin, each with unique behaviors.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Student Class
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course}")

    def view_courses(self):
        print(f"{self.name}'s Courses:", self.courses)


# Teacher Class
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def assign_marks(self, student, marks):
        print(f"{self.name} assigned {marks} marks to {student.name}")

    def display(self):
        super().display()
        print(f"Subject: {self.subject}")


# Admin Class
class Admin(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        print(f"{user.name} added to system")

    def remove_user(self, user):
        self.users.remove(user)
        print(f"{user.name} removed from system")

    def view_users(self):
        print("All Users:")
        for user in self.users:
            print(user.name)


# ------------------ Usage ------------------

# Create objects
s1 = Student("Dibyajyoti", 20, "S101")
t1 = Teacher("Mr. Sharma", 40, "Math")
a1 = Admin("Principal", 50)

# Admin actions
a1.add_user(s1)
a1.add_user(t1)
a1.view_users()

# Student actions
s1.enroll_course("Python")
s1.view_courses()

# Teacher actions
t1.assign_marks(s1, 95)