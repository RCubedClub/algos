def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):

        #Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        key = arr[i]
        j=i-1

        while( j>=0 and arr[j]>key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    
    return arr
