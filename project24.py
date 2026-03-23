#Employee Attendance System Build a loop-based menu system to add, remove, and display employee names stored in a dictionary. Use conditions and loops to control program flow.
emp = {}

while True:
    print("1.Add 2.Remove 3.Show 4.Exit")
    ch = int(input())

    if ch == 1:
        name = input("Enter name: ")
        emp[name] = "Present"

    elif ch == 2:
        name = input("Remove name: ")
        emp.pop(name, None)

    elif ch == 3:
        print(emp)

    else:
        break