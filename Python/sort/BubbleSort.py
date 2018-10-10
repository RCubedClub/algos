def bubblesort(arr):

    length = len(arr)
    swapped = 1    
    # swapped variable is used to reduce unnecessary computations
    # if the remaining list is already sorted

    for i in reversed(range(length)):
        if(swapped==1):
            swapped = 0
            for j in range(i):
                if(arr[j]>arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = 1
    return arr
