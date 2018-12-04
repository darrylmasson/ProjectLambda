


class Sensor(object):
    def __init__(self):
        self.room_number = room_number
        self.sensor_number = sensor_number


    def Reading(self):
        now = now()
        value = self.device.read()
        value = self.ProcessReading(value)
        return (now, value)

    def ProcessReading(self, value):
        return value
