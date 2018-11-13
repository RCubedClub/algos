def isPalindrome(string):
    # Using predefined function to
    # reverse to string print(s)
    reverse = ''.join(reversed(s))

    # Checking if both string are
    # equal or not
    if (string==reverse):
        return True
    return False


def main():
    s = "vishal"

    result = isPalindrome(s)

    if result:
        print("String is palindrome.")
    else:
        print("Not palindrome.")

if __name__ == '__main__':
    main()