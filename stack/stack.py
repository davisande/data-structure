import numpy as np


class Stack:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__top = -1
        self.__values = np.chararray(self.__capacity, unicode=True)

    def stack_up(self, value):
        if self.__is_full_stack():
            print('The stack is full')
        else:
            self.__top += 1
            self.__values[self.__top] = value

    def __is_full_stack(self):
        return self.__top == self.__capacity - 1

    def unstack(self):
        if self.is_empty():
            print('The stack is empty')
        else:
            value = self.__values[self.__top]
            self.__top -= 1
            return value

    def is_empty(self):
        return self.__top == -1

    def size(self):
        return self.__top
