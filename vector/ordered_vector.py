import numpy as np


class OrderedVector:

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

    # O(n)
    def add(self, value):
        if self.last_position == self.capacity - 1:
            print('Maximum capacity reached')
            return

        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i] > value:
                break
            if i == self.last_position:
                position = i + 1

        index_reorder = self.last_position
        while index_reorder >= position:
            self.values[index_reorder + 1] = self.values[index_reorder]
            index_reorder -= 1

        self.values[position] = value
        self.last_position += 1

    # O(n)
    def index_of(self, value):
        for i in range(self.last_position + 1):
            if self.values[i] > value or (i == self.last_position and self.values[i] < value):
                return -1
            if self.values[i] == value:
                return i

    # O(log n)
    def binary_index_of(self, value):
        low_index = 0
        high_index = self.last_position
        index = -1
        keep_search = True
        while keep_search:
            mid_index = int((low_index + high_index) / 2)
            if self.values[mid_index] == value:
                index = mid_index
                keep_search = False
            elif low_index > high_index:
                keep_search = False
            else:
                if self.values[mid_index] < value:
                    low_index = mid_index + 1
                else:
                    high_index = mid_index - 1

        return index

    # O(n)
    def remove(self, value):
        position = self.index_of(value)
        if position == -1:
            return -1
        else:
            for i in range(position, self.last_position):
                self.values[i] = self.values[i + 1]
            self.last_position -= 1

