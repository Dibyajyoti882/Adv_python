class ContactError(Exception):
    pass


class ContactBook:

    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        try:
            if name in self.contacts:
                raise ContactError("Contact already exists")

            if len(phone) != 10:
                raise ContactError("Phone number must be 10 digits")

            self.contacts[name] = phone
            print("Contact added")

        except ContactError as e:
            print(e)

    def search_contact(self, name):
        try:
            if name not in self.contacts:
                raise ContactError("Contact not found")

            print(name, ":", self.contacts[name])

        except ContactError as e:
            print(e)

    def display(self):
        print("All Contacts:")
        for i in self.contacts:
            print(i, ":", self.contacts[i])


c = ContactBook()
c.add_contact("Rahul", "9876543210")
c.add_contact("Rahul", "9876543210")  
c.search_contact("Amit")
c.display()