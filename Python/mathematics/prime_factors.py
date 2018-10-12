import math

def iterative(n):

    list_ = []
    if n%2==0:
        list_.append(2)
        while n % 2 == 0:
            n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n%i==0:
            list_.append(i)
            while n % i == 0:
                n = n / i

    if n > 2:
        list_.append(n)

    return list_


def main():
    n = int(input())

    result = iterative(n)
    print("List of Prime Factors", result)

if __name__ == '__main__':
    main()