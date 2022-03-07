class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song
        self.volume = 0

    def pay_fee(self, room):
        self.wallet -= room.price

    def react_to_song(self, song):
        if song.name == self.favourite_song:
            return "whoo"
        else:
            return "meh"

    def increase_volume(self):
        self.volume += 25