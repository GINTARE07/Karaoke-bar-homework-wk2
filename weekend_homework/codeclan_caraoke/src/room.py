class Room:

    def __init__(self, room, capacity):
        self.room = room 
        self.capacity = 30
        self.guests = []
        # self.customer = customer

    def add_guest(self, guest):
        self.guests.append(guest)

    # def customers_count(self):
    #     return len(self.customer)