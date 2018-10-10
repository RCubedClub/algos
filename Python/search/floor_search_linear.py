from random import randint

"""
Python Code for searching the next greater element than x in array.
If next greater element is present then return the index of that element.
If the same element is present in the array then return the index of the searched element.
Otherwise return None.
"""

def iterative(array, element):
    """
    Perform Linear Search by Iterative Method.
    :param array: Iterable of elements.
    :param element: element to be searched.
    :return: returns value of index of element (if found) else return None.
    """
    next_lower = min(array) - 1
    index = None
    for i in range(len(array)):
        if array[i]==element:
            return i
        elif array[i]<element:
            if next_lower!=max(next_lower, array[i]):
                index = i
                next_lower = max(next_lower, array[i])
    return index


def recursive(array, element, next_lower, low, index):
    """
    Perform Linear Search by Recursive Method.
    :param array: Iterable of elements.
    :param next_lower: store the next lower element.
    :param index: store the index number of the next greater element.
    :param low: traversing variable of an array.
    :param element: element to be searched.
    :return: returns value of index of element (if found) else return None.
    """

    if array[low]==element:
        return low

    if array[low]<element:
        if next_lower != max(next_lower, array[low]):
            index = low
            next_lower = max(next_lower, array[low])

    if low==len(array)-1:
        return index

    return recursive(array, element, next_lower, low+1, index)

def main():
    array = [randint(1,10000) for _ in range(100)]
    print(array)
    element = randint(1,10000)
    print(element)
    result = iterative(array, element)
    if result is None:
        print('Iterative Floor Search : Element not present in array')
    else:
        print('Iterative Floor Search : Element is present at index', result)

    result = recursive(array, element, min(array) - 1, 0, None)
    if result is None:
        print('Recursive Floor Search : Element not present in array')
    else:
        print('Recursive Floor Search : Element is present at index', result)

if __name__ == '__main__':
    main()
