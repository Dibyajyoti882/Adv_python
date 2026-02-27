students = {}  


def add_student():
    name = input("Enter student name: ")
    
    m1 = int(input("Enter marks for Math: "))
    m2 = int(input("Enter marks for Science: "))
    m3 = int(input("Enter marks for English: "))
    
    marks = [m1, m2, m3]   
    
    students[name] = marks
    
    print("Student added successfully")


def show_result():
    name = input("Enter student name: ")
    
    if name in students:
        marks = students[name]
        
        total = marks[0] + marks[1] + marks[2]
        average = total / 3
        
        print("Marks:", marks)
        print("Total:", total)
        print("Average:", average)
        
        grade_data = (90, 80, 70, 60, 50)
        
        if average >= grade_data[0]:
            print("Grade: A")
        elif average >= grade_data[1]:
            print("Grade: B")
        elif average >= grade_data[2]:
            print("Grade: C")
        elif average >= grade_data[3]:
            print("Grade: D")
        elif average >= grade_data[4]:
            print("Grade: E")
        else:
            print("Grade: F")
    else:
        print("Student not found")


while True:
    print("\nGRADE BOOK MENU")
    print("1. Add Student")
    print("2. Show Result")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        show_result()
    elif choice == "3":
        print("Thank you")
        break
    else:
        print("Wrong choice")