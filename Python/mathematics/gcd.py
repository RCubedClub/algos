from random import randint

def iterative(x, y):
    """
    Find the GCD or HCF of two numbers.
    :return: returns the hcf of two numbers.
    """
    x, y = max(x, y), min(x, y)

    while y:
        x, y = y, x%y

    return x


def recursive(x, y):
    """
    Find the GCD or HCF of two numbers.
    :return: returns the hcf of two numbers.
    """
    x, y = max(x, y), min(x, y)
    if y==0:
        return x

    return recursive(y, x%y)

def main():
    x, y = randint(1,10000), randint(1,10000)
    print(x, y)
    result = recursive(x, y)
    print('GCD of two numbers is', result)
    result = iterative(x, y)
    print('GCD of two numbers is', result)


if __name__ == '__main__':
    main()