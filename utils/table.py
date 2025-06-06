import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.file_utils import load_config



class Seat:
    """
    Create a seat defined by:
    occupant: A person assigned to the seat, None by default.
    free: A boolean representing availability, True by default.
    """
    def __init__(self, occupant: str = None, free: bool = True):
        self.occupant = occupant
        self.free = free

    def set_occupant(self, name: str):
        """
        Assigns a person to the seat if available.
        name: The occupant's name.
        """
        if self.free:
            self.occupant = name
            self.free = False

    def remove_occupant(self):
        """
        Removes an occupant and marks the seat as available.
        """
        self.occupant = None
        self.free = True

    def __str__(self) -> str:
        """Returns a readable string of the seat."""
        return f"Seat(occupant={self.occupant if self.occupant else 'Empty'}, free={self.free})"


class Table:

    """
    Represents a table with multiple seats.

    Attributes:
    capacity: Number of seats per table.
    seats: A list containing Seat objects.
    """

    def __init__(self):
        """Initializes a table with dynamic setup from file_utils."""
        config = load_config()
        self.capacity = config.get("seats_per_table", 4)
        self.seats = [Seat() for _ in range(self.capacity)]


    def has_free_spot(self) -> bool:
        """
        Checks if the table has any free spots.
        return: True if a free seat exists, False otherwise.
        """
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name: str) -> bool:
        """
        Assigns a person to an available seat.
        name: The person's name.
        return: True if successfully assigned, False if no available seats.
        """
        

        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        if not self.prevent_lonely_seat():
            return False

    def left_capacity(self) -> int:
        """
        Returns the number of free seats.
        """
        return sum(1 for seat in self.seats if seat.free)

    def add_seat(self):
        """Adds a seat to the table."""
        self.seats.append(Seat())
        self.capacity += 1

    def remove_seat(self):
        """Removes the last seat if capacity is greater than 1."""
        if self.capacity > 1:
            self.seats.pop()
            self.capacity -= 1

    def prevent_lonely_seat(self) -> bool:
        """
        Ensures no one sits alone at a table.
        return: False if only one person would be seated, True otherwise.
        """
        occupied_seats = sum(1 for seat in self.seats if not seat.free)
        return occupied_seats != 1

    def __str__(self) -> str:
        """Returns a readable string of the table."""
        seat_status = ', '.join([seat.occupant if seat.occupant else 'Empty' for seat in self.seats])
        return f"Table(capacity={self.capacity}, seats=[{seat_status}])"