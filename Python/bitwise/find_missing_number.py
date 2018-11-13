import random

def find(array):
    miss = 0
    for i in range(len(array)):
        miss ^= array[i]
        miss ^= i + 1

    return miss


def main():
    arr = [random.randint(1,100) for _ in range(99)]

    result = find(arr)
    print("The missing number is-", result)


if __name__ == '__main__':
    main()
