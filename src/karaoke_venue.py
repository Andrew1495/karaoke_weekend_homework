class Venue:
    def __init__(self, input_name, input_till, input_room_amount):


        self.name = input_name
        self.till = input_till
        self.amount_of_rooms = input_room_amount
        self.rooms = []


    def is_rooms_avaible(self):
        if len(self.rooms) < self.amount_of_rooms:
            return True
        else:
            return False