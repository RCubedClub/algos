
def series(n, bool=False): 
    """
    :param bool: If bool=True, then the function will return the boolean list of the prime numbers.
                If bool=False, then the function will return the list of prime number less than n+1.
    :param n: Prime Number less than n.
    :return: returns None if n is 0 or 1 otherwise returns the list of prime numbers less than n.
    """ 

    # If n is less than 2, return None because no prime number is less than 2.
    if n<2:
        return None

    prime = [True]*(n+1)
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n+1, p): 
                prime[i] = False
        p += 1

    if bool:
        return prime
    else:
        list_ = []
        for i in range(2, n+1):
            if prime[i]:
                list_.append(i)
        return list_


def main():
    n = int(input())

    result = series(n)
    if result is None:
        print("Enter number greater than 2")
    else:
        print("List of Prime Numbers", result)

    result = series(n, bool=True)
    if result is None:
        print("Enter number greater than 2")
    else:
        print("Boolean list for prime numbers", result)

if __name__ == '__main__':
    main()