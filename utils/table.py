
"""create seat class"""
class Seat:
    """defined by: occupant(person), which is empty by default and availability (free -> true or false), which is true by default"""
    def __init__(self, occupant: str = None, free: bool = True):
        self.occupant = occupant
        self.free = free

    """create occupancy paramaters"""    
    def set_occupant(self, name:str):
        """assign a person to the seat and set it's availability to false"""
        if self.free:
            self.occupant = name
            self.free = False

    def remove_occupant(self):
        """remove a person from a seat and set it to free"""
        self.occupant = None
        self.free = True

from typing import List
"""create table class"""
class Table:
    """define a table by its capacity and the seats filled or free"""
    def __init__(self, capacity: int, seats: List[Seat]):
        self.capacity = capacity
        self.seats = seats

    def has_free_spot(self)

    def assign_seat(self, name: str):
        """assign person to seat"""
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False
    
    def

