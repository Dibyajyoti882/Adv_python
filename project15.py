class BookingError(Exception):
    pass


class Flight:

    def __init__(self):
        self.seats = 5

    def book_ticket(self, name, seats):
        try:
            if seats > self.seats:
                raise BookingError("Seats not available")

            self.seats -= seats
            print("Ticket booked for", name)

        except BookingError as e:
            print(e)

    def cancel_ticket(self, seats):
        self.seats += seats
        print("Ticket cancelled")

    def show_seats(self):
        print("Available seats:", self.seats)


f = Flight()

f.book_ticket("Rahul", 2)
f.book_ticket("Amit", 4)
f.cancel_ticket(1)
f.show_seats()