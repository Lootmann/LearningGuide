from datetime import datetime, timedelta


class Clock:
    def __init__(self, hour, minute):
        advance, minute = divmod(minute, 60)
        _, hour = divmod(hour + advance, 24)
        self.time = datetime(2022, 1, 1, hour, minute, 0)

    def __repr__(self):
        return f"Clock({self.time.hour}, {self.time.minute})"

    def __str__(self):
        return "{:02d}:{:02d}".format(self.time.hour, self.time.minute)

    def __eq__(self, other: "Clock"):
        return self.time == other

    def __add__(self, minutes):
        self.time += timedelta(minutes=minutes)
        return str(self)

    def __sub__(self, minutes):
        self.time -= timedelta(minutes=minutes)
        return str(self)
