class Group:
    def __init__(self):
        self.group = []

    def add_to_group(self, guests):
        self.group.append(guests)

    def remove_from_group(self, guest):
        self.group.remove(guest)
    

    