import numpy as np


class NotOrderedVector:

    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, int)

    # O(n)
    def print(self):
        if self.last_position == -1:
            print('The vector is empty')
        else:
            for i in range(self.last_position + 1):
                print(i, ' - ', self.values[i])

    # O(1) - O(2)
    def add(self, value):
        if self.last_position == self.capacity - 1:
            print('Maximum capacity reached')
        else:
            self.last_position += 1
            self.values[self.last_position] = value

    # O(n)
    def index_of(self, value):
        for i in range(self.last_position + 1):
            if value == self.values[i]:
                return i
        return -1

    # O(n)
    def remove(self, value):
        position = self.index_of(value)
        if position == -1:
            return -1
        else:
            for i in range(position, self.last_position):
                self.values[i] = self.values[i + 1]
            self.last_position -= 1
