import numpy as np


class Deque:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__initial_index = 0
        self.__final_index = 0
        self.__length = 0
        self.__values = np.empty(self.__capacity, int)

    def __is_full(self):
        return self.__length == self.__capacity

    def __is_empty(self):
        return self.__length == 0

    def add_beginning(self, value):
        if self.__is_full():
            print("The deque is full")
            return

        if self.__length > 0:
            if self.__initial_index == self.__capacity - 1:
                self.__initial_index = 0
            elif self.__initial_index == 0:
                self.__initial_index = self.__capacity - 1
            else:
                self.__initial_index -= 1

        self.__values[self.__initial_index] = value
        self.__length += 1

    def add_end(self, value):
        if self.__is_full():
            print("The deque is full")
            return

        if self.__length == 0:
            self.__initial_index = 0
            self.__final_index = 0
        elif self.__final_index == self.__capacity - 1:
            self.__final_index = 0
        else:
            self.__final_index += 1

        self.__values[self.__final_index] = value
        self.__length += 1

    def remove_beginning(self):
        if self.__is_empty():
            print("The deque is empty")
            return

        if self.__length == 0:
            self.__initial_index = 0
            self.__final_index = 0
        elif self.__initial_index == self.__capacity - 1:
            self.__initial_index = 0
        else:
            self.__initial_index += 1
        self.__length -= 1

    def remove_end(self):
        if self.__is_empty():
            print("The deque is empty")
            return

        if self.__final_index == 0:
            self.__final_index = self.__capacity - 1
        else:
            self.__final_index -= 1
        self.__length -= 1

    def get_beginning(self):
        if self.__is_empty():
            print("The deque is empty")
            return

        return self.__values[self.__initial_index]

    def get_end(self):
        if self.__is_empty():
            print("The deque is empty")
            return

        return self.__values[self.__final_index]

