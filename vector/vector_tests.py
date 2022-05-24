from vector.NotOrderedVector import NotOrderedVector


def tests():
    vector = NotOrderedVector(5)
    vector.print()

    vector.add(9)
    vector.add(2)
    vector.add(5)
    vector.add(1)
    vector.add(8)
    vector.print()
    vector.add(3)

    index = vector.index_of(1)
    print(index)
    index = vector.index_of(9)
    print(index)
    index = vector.index_of(4)
    print(index)

    vector.remove(5)
    vector.print()
    print('---')
    vector.remove(8)
    vector.print()
    print('---')
    vector.remove(9)
    vector.print()
    print('---')
    index = vector.remove(4)
    print(index)


if __name__ == '__main__':
    tests()
