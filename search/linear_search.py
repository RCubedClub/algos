from random import randint

"""
Python code for linearly search x in arr[].  If x
is present then return its  location,  otherwise
return None.
"""

def iterative(array, element):
    """
    Perform Linear Search by Iterative Method.
    :param array: Iterable of elements.
    :param element: element to be searched.
    :return: returns value of index of element (if found) else return None.
    """
    for i in range(len(array)):

        if array[i] == element:
            return i

    return None


def main():
    array = [randint(1,10000) for _ in range(100)]
    element = 13
    result = iterative(array, element)
    result = iterative(array, element)
    if result is None:
        print('Iterative Linear Search : Element not present in array')
    else:
        print('Iterative Linear Search : Element is present at index', result)


if __name__ == '__main__':
    main()