from utils.table import Table
"""
Import the Table class
"""
import random
"""
To use random.suffle
"""

class Openspace:
    def __init__(self, number_of_tables=6):
        """
        Creating a room with 6 tables and add to a list

        """
        self.number_of_tables = number_of_tables
        self.tables = []
        
        count = 0
        while count < 6:
            table() = Table()
            self.tables.append(Table)
            count +=1


    def organize(self, names):
        """
        We need a method to randomly assigns names to seats
        """
    
    random.shuffle(names)

    for name in names:
        seated = False
        """
        Assume they are not seated yet and go through the tables to see if there is any free seat
        """

    for table in self.tables:
        if table.has_free_spot():
            table.assigned_seat(name)
            seated = True
            break

    if  not seated:
            print(f"NO free seat for: {name}")



