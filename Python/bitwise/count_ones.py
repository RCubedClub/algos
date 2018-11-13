from random import randint

def recursive(n):
    """Using Brian Kernighan’s Algorithm. (Recursive Approach)"""

    """
    Count the occurrence of count bits in a binary representation of a number.
    :param n: The binary representation of a number.
    :return: returns the count of 1s in a n.
    """

    if not n:
        return 0
    return 1 + recursive(n & (n-1))


def iterative(n):
    """Using Brian Kernighan’s Algorithm. (Iterative Approach)"""

    """
    Count the occurrence of count bits in a binary representation of a number.
    :param n: The binary representation of a number.
    :return: returns the count of 1s in a n.
    """

    count = 0
    while n:
        n &= (n-1)
        count += 1
    return count


def main():
    num = randint(1, 1000)
    print(num)
    num = int(bin(num)[2:])

    result = recursive(num)
    print("Recursive : ", result)
    result = iterative(num)
    print("Iterative : ", result)


if __name__ == '__main__':
    main()