from random import randint

def iterative(arr, summation, sort=True):

    if sort:
        arr.sort()

    n = len(arr)
    l, r = 0, n-1

    while l<r:
        if arr[l]+arr[r]==summation:
            return True
        elif arr[l]+arr[r]<summation:
            l+=1
        else:
            r-=1

    return False


def recursive(arr, summation, l, r, sort=True):

    if sort:
        arr.sort()
        return recursive(arr, summation, l, r, sort=False)

    if l>=r:
        return False
    if arr[l]+arr[r]==summation:
        return True
    elif arr[l]+arr[r]<summation:
        return recursive(arr, summation, l+1, r)
    else:
        return recursive(arr, summation, l, r-1)


def main():
    array = [randint(1,100) for _ in range(100)]
    element = randint(1,1000)

    print(array)
    print(element)

    result = recursive(array, element, 0, len(array)-1)
    if result:
        print('Recursive Search : Elements present in array')
    else:
        print('Recursive Search : Elements are not present.')

    result = iterative(array, element)
    if result:
        print('Iterative Search : Elements present in array')
    else:
        print('Iterative Search : Elements are not present.')


if __name__ == '__main__':
    main()