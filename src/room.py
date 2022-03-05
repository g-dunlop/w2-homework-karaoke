from xml.etree.ElementPath import prepare_predicate


class Room:
    def __init__(self, name, price, capacity):
        self.name = name
        self.price = price
        self.capacity = capacity
        self.bill = 0
        self.guests = []
        self.songs = []
        self.drinks = {}


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

    def add_entry_fee_to_room_bill(self):
        self.bill += self.price


    def check_in_guest(self, guest):
        if self.check_room_has_space() == False:
            return "Sorry, we're full"
        else:
            if self.check_funds(guest) == False:
                return "Sorry, you can't afford karaoke today."
            else:
                self.add_guest(guest)
                # guest.pay_fee(self)
                self.add_entry_fee_to_room_bill()
                # this could be an add_to_bill function

    

    def add_drink(self, drink):
        if drink in self.drinks:
            self.drinks[drink] += 1
        else:
            self.drinks[drink] = 1

    def running_drinks_total(self, drink):
        if drink in self.drinks:
            return self.drinks[drink]
        else:
            return 0

    def total_drinks_value(self):
        total = 0

        for drink in self.drinks:
            total += (drink.price * self.drinks[drink])
        return total
                

    def add_drinks_bill_to_room_bill(self):
        drinks_bill = self.total_drinks_value()
        self.bill += drinks_bill

    def split_bill(self):
        split_bill = self.bill / len(self.guests)
        return split_bill