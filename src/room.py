from src.group import Group

class Room:
    def __init__(self, input_name, input_room_capacity):
        self.name = input_name
        self.room_capacity = input_room_capacity
        self.songs = []
        self.guests = []

    

    def add_guest_room(self, guest):
        self.guests.append(guest)

    def add_group_to_room(self, group):
        for guest in group:
            