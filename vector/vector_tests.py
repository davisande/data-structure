from not_ordered_vector import NotOrderedVector
from ordered_vector import OrderedVector


def test_not_ordered_vector():
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


def test_ordered_vector():
    vector = OrderedVector(5)
    vector.print()

    vector.add(3)
    vector.add(5)
    vector.add(2)
    vector.add(1)
    vector.add(4)
    vector.print()
    vector.add(6)

    index = vector.index_of(3)
    print(index)
    index = vector.index_of(1)
    print(index)
    index = vector.index_of(5)
    print(index)
    index = vector.index_of(6)
    print(index)

    print('---')

    index = vector.binary_index_of(3)
    print(index)
    index = vector.binary_index_of(1)
    print(index)
    index = vector.binary_index_of(5)
    print(index)
    index = vector.binary_index_of(6)
    print(index)

    vector.remove(3)
    vector.print()
    print('---')
    vector.remove(1)
    vector.print()
    print('---')
    vector.remove(5)
    vector.print()
    print('---')
    index = vector.remove(6)
    print(index)


if __name__ == '__main__':
    # test_not_ordered_vector()
    test_ordered_vector()
