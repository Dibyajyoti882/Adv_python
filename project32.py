#Implement a Library Management System that uses parameterized constructors to initialize books and members and destructors to log when books are removed.
class Book:
    def __init__(self, name):
        self.name = name
        print(name, "Book added")

    def __del__(self):
        print(self.name, "Book removed")


library = []

while True:
    print("\n1. Add Book")
    print("2. Remove Book")
    print("3. Show Books")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Enter book name: ")
        b = Book(name)
        library.append(b)

    elif ch == 2:
        name = input("Enter book name to remove: ")
        found = False

        for b in library:
            if b.name == name:
                library.remove(b)
                del b   # destructor will run
                found = True
                break

        if not found:
            print("Book not found")

    elif ch == 3:
        print("Books in Library:")
        for b in library:
            print(b.name)

    elif ch == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")