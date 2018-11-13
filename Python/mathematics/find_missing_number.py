import random

def find(array):
    summation = sum(array)
    n = len(array)
    total = n*(n+1)//2
    miss = total - summation

    return miss


def main():
    arr = [i for i in range(99)]

    print(arr)
    result = find(arr)
    print("The missing number is-", result)


if __name__ == '__main__':
    main()
