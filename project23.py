#Create a contact book using a dictionary with options to add, search, delete, and list contacts.
contacts = {}

while True:
    print("1.Add 2.Search 3.Delete 4.Show 5.Exit")
    ch = int(input())

    if ch == 1:
        name = input("Name: ")
        num = input("Number: ")
        contacts[name] = num

    elif ch == 2:
        name = input("Search name: ")
        print(contacts.get(name, "Not found"))

    elif ch == 3:
        name = input("Delete name: ")
        contacts.pop(name, None)

    elif ch == 4:
        print(contacts)

    else:
        break