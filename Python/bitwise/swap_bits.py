
def swap_pair(num):

    """
    Swap the bits in a binary representation of a number.
    :param num: The number.
    :return: returns the integer after swapping the bits of the initial number.
    """

    # odd bit arithmetic right shift 1 bit
    odd = (num & int('AAAAAAAA', 16)) >> 1
    # even bit left shift 1 bit
    even = (num & int('55555555', 16)) << 1
    return odd | even


def main():
    num = 41
    result = swap_pair(num)

    print(result)

if __name__ == '__main__':
    main()