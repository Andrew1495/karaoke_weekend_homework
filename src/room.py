

class Room:
    def __init__(self, input_name, input_room_capacity):
        self.name = input_name
        self.room_capacity = input_room_capacity
        self.songs = []
        self.guests = []

    

    def add_guest_room(self, guest, venue):
        if len(self.guests) < self.room_capacity and guest.wallet >= venue.price:
            self.guests.append(guest)

    def remove_guest(self, guest):
        for g in self.guests:
            if g.name == guest.name:
                self.guests.remove(g)

    def add_song_room(self,song):
        self.songs.append(song)

    def remove_song(self,song):
        for s in self.songs:
            if s.name == song.name:
                self.songs.remove(s)

    