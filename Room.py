


class Room(object):
    def __init__(self):
        self.room_number = room_number
        self.sensors = []


class Bathroom(Room):
    def __init__(self):
        super().__init__(self)
        self.shower = Shower()
