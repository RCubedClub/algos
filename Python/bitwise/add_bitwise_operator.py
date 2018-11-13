def add_bitwise_operator(x, y):
    """
    Perform Linear Search by Iterative Method.
    :param array: Iterable of elements.
    :param element: element to be searched.
    :return: returns value of index of element (if found) else return None.
    """
    x, y = min(x, y), max(x, y)
    while y:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x


def main():
    x, y = 9, 3
    result = add_bitwise_operator(x, y)

    print(result)


if __name__ == '__main__':
    main()