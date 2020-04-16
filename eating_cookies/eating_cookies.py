#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    # fib setup fn = f(n-1) + f(n+2)
    # __base_case__
    # if n = 1 return 1
    # if n = 0 return 0

    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        # I can either either eat 1 - 2 - 3 cookies at a time
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
    # print(n)


print(eating_cookies(10))
if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
