from src.room import Room

class Venue:
    def __init__(self, input_name, input_till, input_room_amount, input_price):


        self.name = input_name
        self.till = input_till
        self.amount_of_rooms = input_room_amount
        self.rooms = []
        self.price = input_price
        self.menu = []

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

    def add_item_menu(self, item):
        already_have = False
        for i in self.menu:
            if i.name == item.name:
                already_have = True
        if already_have == False:
            self.menu.append(item)
        
    def find_item_buy_name(self, item):
        for i in self.menu:
            if i.name == item:
                return i

    def add_item_to_guest(self, guest, item):
        guest.item_list.append(item)
        for i in self.menu:
            if item.name == i.name:
                i.quanity -= 1



    def customer_pay_tab(self, guest):
        tab =0
        for i in guest.item_list:
            tab += i.price
        guest.wallet -= tab + self.price
        self.till += tab + self.price

    def check_room_full(self):
        for room in self.rooms:
            if len(room) == room.room_capacity:
                return True
        else:
            return False

    def add_room(self, room):
        self.rooms.append(room)

    def setting_up_rooms(self, room_size):
        i = 1
        while len(self.rooms) < self.amount_of_rooms:
            self.rooms.append(Room(f"room {i}", room_size))
            i += 1
        

