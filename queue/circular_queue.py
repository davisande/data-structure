import numpy as np


class CircularQueue:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__initial_index = 0
        self.__final_index = -1
        self.__length = 0
        self.__values = np.empty(capacity, int)

    def __is_empty(self):
        return self.__length == 0

    def __is_full(self):
        return self.__length == self.__capacity

    def add(self, value):
        if self.__is_full():
            print('The queue is full')
            return

        if self.__final_index == self.__capacity - 1:
            self.__final_index = -1
        self.__final_index += 1
        self.__values[self.__final_index] = value
        self.__length += 1

    def dequeue(self):
        if self.__is_empty():
            print('The queue is empty')
            return

        current_value = self.__values[self.__initial_index]
        self.__initial_index += 1
        if self.__initial_index == self.__capacity - 1:
            self.__initial_index = 0
        self.__length -= 1
        return current_value

    def get(self):
        if self.__is_empty():
            return -1
        return self.__values[self.__initial_index]
