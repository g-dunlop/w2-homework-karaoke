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

    def check_room_has_space(self):
        if len(self.guests) < self.capacity:
            return True
        else:
            return False

    def check_funds(self, guest):
        if guest.wallet < self.price:
            return False
        else:
            return True

    def check_in_guest(self, guest):
        if self.check_room_has_space() == False:
            return "Sorry, we're full"
        else:
            if self.check_funds(guest) == False:
                return "Sorry, you can't afford karaoke"
            else:
                self.add_guest(guest)
                guest.pay_fee(self)
            

    