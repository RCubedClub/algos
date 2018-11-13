from random import randint

def iterative(arr, summation):
    """
    Perform Two Sum by Iterative Method.
    :param arr: Iterable of elements.
    :param summation: sum to be searched.
    :return: returns true if found, else return None.
    """
    hash = set()

    for i in range(len(arr)):
        temp = summation-arr[i]
        if temp>=0 and temp in hash:
            return True
        hash.add(arr[i])

    return False


def recursive(arr, summation, i=0, hash=set()):
    """
    Perform Two Sum by Recursive Method.
    :param arr: Iterable of elements.
    :param summation: sum to be searched.
    :return: returns true if found, else return None.
    """
    if i==len(arr):
        return False

    temp = summation - arr[i]
    if temp>=0 and temp in hash:
        return True

    hash.add(arr[i])

    return recursive(arr, summation, i+1, hash)


def main():
    array = [randint(1,100) for _ in range(100)]
    element = randint(1,300)

    print(array)
    print(element)

    result = recursive(array, element)
    if result:
        print('Recursive : Elements are present in array')
    else:
        print('Recursive : Elements are not present.')
    result = iterative(array, element)
    if result:
        print('Iterative : Elements are present in array')
    else:
        print('Iterative : Elements are not present.')


if __name__ == '__main__':
    main()