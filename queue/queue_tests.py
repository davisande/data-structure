from circular_queue import CircularQueue
from priority_queue import PriorityQueue


def circular_queue_test():
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

def priority_queue_test():
    queue = PriorityQueue(5)
    value = queue.get()
    print(value)

    queue.add(1)
    value = queue.get()
    print(value)
    queue.add(5)
    value = queue.get()
    print(value)
    queue.add(2)
    queue.add(2)
    queue.add(1)
    queue.print()

    value = queue.dequeue()
    print(value)
    queue.dequeue()
    queue.dequeue()
    value = queue.dequeue()
    print(value)
    value = queue.get()
    print(value)


if __name__ == '__main__':
    print('CIRCULAR QUEUE TEST')
    print('-------------------')
    circular_queue_test()
    print('PRIORITY QUEUE TEST')
    print('-------------------')
    priority_queue_test()
