# -*- coding: utf-8 -*-

from random import randint
import math

def pow_mod(a, b, r):
    """ Returns a**b (mod r) """
    """ Complexity: O( log(B) * log^2(r) ) """
    ans, buff = 1, a
    while(b):
        if b & 1:
            ans = (ans * buff) % r
        buff = (buff * buff) % r
        b >>= 1
    return ans

def gcd(a, b):
    """ Returns gcd(a, b) """
    """ Complexity: O( log^3(N) ) """
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a

def miller_rabin(n, k=50):
    """
    Miller-Rabin Primality Test
    Returns true if n is a (probable) prime
    Returns false if n is a composite number
    """
    n = int(abs(n))
    if n <= 7:
        return [False, False, True, True, False, True, False, True][n]

    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        s = s + 1
        d = d >> 1
    for _ in range(k):
        a = randint(2, n-2)
        x = pow_mod(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(s-1):
            x = pow_mod(x, 2, n)
            if x == 1:
                return False
            elif x == n - 1:
                a = 0
                break
        if a:
            return False
    return True

def is_prime(n):
    n = int(abs(n))
    if n <= 7:
        return [False, False, True, True, False, True, False, True][n]

    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False

    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def main():
    for n in range(1, 10000000):
        if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
            continue

        if miller_rabin(n, 10):
            if not is_prime(n):
                print n
    print 'OK'

if __name__ == '__main__':
    main()
