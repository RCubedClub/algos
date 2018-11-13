import random

def is_power_of_two(num):
    return num>0 and not num&(num-1)


def main():
    n = random.randint(1, 10000)
    result = is_power_of_two(n)

    if result:
        print(str(n) + " is the power of 2.")
    else:
        print(str(n) + " is not the power of 2.")


if __name__ == '__main__':
    main()