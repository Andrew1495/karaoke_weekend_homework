class Venue:
    def __init__(self, input_name, input_till, input_room_amount, input_price):


        self.name = input_name
        self.till = input_till
        self.amount_of_rooms = input_room_amount
        self.rooms = []
        self.price = input_price


    def is_rooms_avaible(self):
        if len(self.rooms) < self.amount_of_rooms:
            return True
        else:
            return False

    def guest_can_afford(self, guest, item):
        current_tab = 0
        for i in guest.item_list:
            current_tab += i.price
        if guest.wallet >= current_tab + item.price:
            return True
        else:
            return False