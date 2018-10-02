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
    next_greater = max(array) + 1
    index = None
    for i in range(len(array)):
        if array[i]==element:
            return i
        elif array[i]>element:
            if next_greater!=min(next_greater, array[i]):
                index = i
            next_greater = min(next_greater, array[i])
    return index


def recursive(array, element, next_greater, low, index):

    if array[low]==element:
        return low

    if array[low]>element:
        if next_greater != min(next_greater, array[low]):
            index = low
        next_greater = min(next_greater, array[low])

    if low==len(array)-1:
        return index

    return recursive(array, element, next_greater, low+1, index)

def main():
    array = [randint(1,10000) for _ in range(100)]
    print(array)
    element = randint(1,10000)
    print(element)
    result = iterative(array, element)
    if result is None:
        print('Iterative Ceil Search : Element not present in array')
    else:
        print('Iterative Ceil Search : Element is present at index', result)

    result = recursive(array, element, max(array)+1, 0, None)
    if result is None:
        print('Recursive Ceil Search : Element not present in array')
    else:
        print('Recursive Ceil Search : Element is present at index', result)

if __name__ == '__main__':
    main()
