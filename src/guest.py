class Guest:
    def __init__(self, input_name, input_wallet, input_fav_song):
        self.name = input_name
        self.wallet = input_wallet
        self.fav_song = input_fav_song
        self.item_list = []

    
    def has_fav_song(self, room):
        for s in room.songs:
            if s.name == self.fav_song:
                return "wooooo"
