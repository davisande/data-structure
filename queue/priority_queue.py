import numpy as np


class PriorityQueue:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__length = 0
        self.__values = np.empty(self.__capacity, int)

    def __is_empty(self):
        return self.__length == 0

    def __is_full(self):
        return self.__length == self.__capacity

    def add(self, value):
        if self.__is_full():
            print('The queue is full')
            return

        if self.__length == 0:
            self.__values[self.__length] = value
        else:
            inclusion_index = self.__length - 1
            while inclusion_index >= 0:
                if value >= self.__values[inclusion_index]:
                    self.__values[inclusion_index + 1] = self.__values[inclusion_index]
                else:
                    break
                inclusion_index -= 1
            self.__values[inclusion_index + 1] = value
        self.__length += 1

    def dequeue(self):
        if self.__is_empty():
            print('The queue is empty')
            return

        value = self.__values[self.__length - 1]
        self.__length -= 1
        return value

    def get(self):
        if self.__is_empty():
            return -1
        return self.__values[self.__length - 1]

    def print(self):
        print(self.__values)
