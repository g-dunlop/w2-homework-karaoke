import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song
from src.drink import Drink

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Room A", 10, 4)
        self.room_2 = Room("Room B", 10, 8)
        self.guest = Guest("Bob", 50, "All Along the Watchtower")
        self.guest_2 = Guest("Joni", 25, "Both Sides Now")
        self.guest_3 = Guest("Jimi", 35, "All Along the Watchtower")
        self.guest_4 = Guest("Mick", 80, "Wild Horses")
        self.guest_5 = Guest("Bon", 5, "Highway to Hell")
        self.drink_1 = Drink("Vodka", 2)
        self.drink_2 = Drink("Whiskey", 2.50)
        self.song = Song("House of the Rising Sun", "The Animals", "Classic Rock")
        self.song_2 = Song("Barbie Girl", "Aqua", "pop")

    def test_room_has_name(self):
        self.assertEqual("Room A", self.room.name)

    def test_room_has_price(self):
        self.assertEqual(10, self.room.price)

    def test_room_has_capacity(self):
        self.assertEqual(4, self.room.capacity)

    def test_can_add_guest(self):
        self.room.add_guest(self.guest)
        self.assertEqual(1, len(self.room.guests))

    def test_can_check_out_guest(self):
        self.room.add_guest(self.guest)
        self.room.remove_guest(self.guest)
        self.assertEqual(0, len(self.room.guests))

    def test_room_has_space_for_guest(self):
        self.room.check_room_has_space()
        self.assertEqual(True, self.room.check_room_has_space())

    def test_room_is_already_full(self):
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest_2)
        self.room.add_guest(self.guest_3)
        self.room.add_guest(self.guest_4)
        self.room.check_room_has_space()
        self.assertEqual(False, self.room.check_room_has_space())

    def test_guest_has_enough_money(self):
        self.room.check_funds(self.guest)
        self.assertEqual(True,self.room.check_funds(self.guest))

    def test_guest_does_not_have_enough_money(self):
        self.room.check_funds(self.guest_5)
        self.assertEqual(False, self.room.check_funds(self.guest_5))
        
    def test_check_in_guest_entry_given(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual(1, len(self.room.guests))

    def test_check_in_guests_entry_given(self):
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest_2)
        self.room.check_in_guest(self.guest_3)
        self.assertEqual(3, len(self.room.guests))

    def test_check_in_5_guests_sorry_bon_full(self):
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest_2)
        self.room.check_in_guest(self.guest_3)
        self.room.check_in_guest(self.guest_4)
        self.room.check_in_guest(self.guest_5)
        self.assertEqual(4, len(self.room.guests))

    def test_check_in_lack_of_funds(self):
        self.room.check_in_guest(self.guest_5)
        self.assertEqual(0, len(self.room.guests))

    def test_room_has_bill(self):
        self.assertEqual(0, self.room.bill)

    def test_can_add_to_room_bill(self):
        self.room.add_entry_fee_to_room_bill()
        self.assertEqual(10, self.room.bill)

    def test_can_add_several_guests_to_room_bill(self):
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest_2)
        self.room.check_in_guest(self.guest_3)
        self.room.check_in_guest(self.guest_4)
        self.assertEqual(40, self.room.bill)

    def test_can_add_drink(self):
        self.room.add_drink(self.drink_2)
        self.assertEqual(1, self.room.running_drinks_total(self.drink_2))


    def test_total_drinks_value(self):
        self.room.add_drink(self.drink_2)
        self.room.add_drink(self.drink_1)
        self.assertEqual(4.50, self.room.total_drinks_value())

        self.assertEqual

    def test_can_add_drinks_orders_to_room_bill(self):
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest_2)
        self.room.add_drink(self.drink_2)
        self.room.add_drink(self.drink_1)
        self.room.add_drinks_bill_to_room_bill()
        self.assertEqual(24.50, self.room.bill)
        
    def test_can_split_the_bill(self):
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest_2)
        self.room.add_drink(self.drink_2)
        self.room.add_drink(self.drink_1)
        self.room.add_drinks_bill_to_room_bill()
        self.assertEqual(12.25, self.room.split_bill())