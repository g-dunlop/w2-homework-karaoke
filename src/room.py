from xml.etree.ElementPath import prepare_predicate


class Room:
    def __init__(self, name, price, capacity):
        self.name = name
        self.price = price
        self.capacity = capacity
        self.guests = []
        self.songs = []


    def add_guest(self, guest):
        self.guests.append(guest)

    def remove_guest(self,guest):
        self.guests.remove(guest)

    def check_room_has_space(self, guests, capacity):
        if len(guests) < capacity:
            return True
        else:
            return False

    def check_funds(self, guest):
        if guest.wallet < self.price:
            return False
        else:
            return True

    # def check_in_guest
    