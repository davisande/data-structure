from circular_deque import Deque


def deque_test():
    deque = Deque(5)

    print('INCLUSION FULL DEQUE')
    print('--------------------')
    deque.add_beginning(1)
    deque.add_beginning(2)
    deque.add_end(3)
    deque.add_end(4)
    deque.add_end(5)
    value = deque.get_beginning()
    print(value)
    value = deque.get_end()
    print(value)

    print('REMOVAL OF THE END')
    print('--------------------')
    deque.remove_end()
    value = deque.get_beginning()
    print(value)
    value = deque.get_end()
    print(value)

    print('REMOVAL OF THE BEGINNING')
    print('--------------------')
    deque.remove_beginning()
    value = deque.get_beginning()
    print(value)
    value = deque.get_end()
    print(value)

    print('REMOVE ALL')
    print('--------------------')
    deque.remove_beginning()
    deque.remove_beginning()
    deque.remove_beginning()

    print('ADD IN THE END')
    print('--------------------')
    deque.add_end(2)
    value = deque.get_beginning()
    print(value)
    value = deque.get_end()
    print(value)

    print('ADD IN THE BEGINNING')
    print('--------------------')
    deque.add_beginning(1)
    value = deque.get_beginning()
    print(value)
    value = deque.get_end()
    print(value)


if __name__ == '__main__':
    deque_test()
