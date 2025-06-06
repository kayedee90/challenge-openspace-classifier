"""create seat class"""


class Seat:
    """defined by: occupant(person), which is empty by default and availability (free -> true or false), which is true by default"""

    def __init__(self, occupant: str = None, free: bool = True):
        self.occupant = occupant
        self.free = free

    """create occupancy paramaters"""

    def set_occupant(self, name: str):
        """assign a person to the seat and set it's availability to false"""
        if self.free:
            self.occupant = name
            self.free = False

    def remove_occupant(self):
        """remove a person from a seat and set it to free"""
        self.occupant = None
        self.free = True


"""create table class"""


class Table:
    """define a table, set its capacity to 4 seats"""

    def __init__(self):
        self.capacity = 4
        self.seats = [Seat() for _ in range(self.capacity)]

    def has_free_spot(self):
        """check if table has any free spots"""
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name: str):
        """assign person to seat, if any seats are free"""
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False

    def left_capacity(self):
        """returns the capacity left"""
        return sum(1 for seat in self.seats if seat.free)
