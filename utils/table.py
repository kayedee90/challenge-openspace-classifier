class Table:
    def __init(self, capacity=4):
        self._capacity = capacity
        self._seats = []

        count = 0
        while count < capacity:
            seat = Seat()
            self._seats.append(seat)
            count = count + 1