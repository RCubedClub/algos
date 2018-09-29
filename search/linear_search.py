"""
Python code for linearly search x in arr[].  If x
is present then return its  location,  otherwise
return -1
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