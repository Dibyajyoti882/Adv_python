#Build a Student Record System using nested dictionaries/lists to add students, update marks, compute averages, and find toppers.
students = {}

for i in range(2):
    name = input("Enter name: ")
    marks = list(map(int, input("Enter marks: ").split()))
    students[name] = marks

for k, v in students.items():
    avg = sum(v)/len(v)
    print(k, "Average:", avg)