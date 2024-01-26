class Seat:
    def __init__(self, free: bool, occupant: str):
        self.free = free
        self.occupant = occupant

    def set_ocupation(self, name):
        self.occupant = name
        self.free = False

    def remove_occupant(self):
        self.occupant = "Empty"
        self.free = True


class Table:
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = [Seat(True, "") for i in range(capacity)]

    def has_free_spot(self):
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_ocupation(name)
                break

    def capacity_left(self):
        return (self.capacity - len(self.seats))
