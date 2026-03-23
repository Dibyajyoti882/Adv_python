# Student Record ManagerCreate a system where a user can enter multiple student records (name, roll number, marks). Use loops to add records and conditions to filter students based on pass/fail criteria. Store data using dictionaries and lists.
students = []

for i in range(3):
    name = input("Name: ")
    roll = input("Roll: ")
    marks = int(input("Marks: "))
    students.append({"name": name, "roll": roll, "marks": marks})

for s in students:
    if s["marks"] >= 40:
        print(s["name"], "Pass")
    else:
        print(s["name"], "Fail")