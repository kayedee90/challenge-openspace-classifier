class Seat:
    """
    Create a seat defined by:
    occupant: A person assigned to the seat, None by default.
    free: A boolean representing availability, True by default.
    """
    def __init__(self, occupant: str = None, free: bool = True):
        self.occupant = occupant
        self.free = free

    """create occupancy paramaters"""

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
        """Returns a readable string of the seats."""
        return f"Seat(occupant={self.occupant if self.occupant else 'Empty'}, free={self.free})"


class Table:
    """
    Represents a table with multiple seats.
    capacity (int): The number of seats per table, fixed at 4.
    seats (list of Seat): A list containing Seat objects.
    """

    def __init__(self):
        self.capacity = 4
        self.seats = [Seat() for _ in range(self.capacity)]

    def has_free_spot(self):
        """
        Function to check if table has any free spots
        """
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name: str):
        """
        Assigns a person to an available seat.
        name: The person's name.
        return: True if successfully assigned, False if no available seats
        """
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False

    def left_capacity(self):
        """
        Function that returns the number of free seats
        """
        return sum(1 for seat in self.seats if seat.free)
    
    def __str__(self) -> str:
        """Returns a readable string of the table."""
        return f"Table(capacity={self.capacity}, free_seats={self.left_capacity()})"