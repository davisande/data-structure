from circular_queue import CircularQueue


def queue_test():
    queue = CircularQueue(5)
    value = queue.get()
    print(value)

    queue.add(1)
    value = queue.get()
    print(value)
    queue.add(2)
    queue.add(3)
    queue.add(4)
    queue.add(5)
    value = queue.get()
    print(value)
    queue.add(6)

    queue.dequeue()
    value = queue.dequeue()
    print(value)

    queue.add(6)
    queue.add(7)
    value = queue.get()
    print(value)


if __name__ == '__main__':
    queue_test()
