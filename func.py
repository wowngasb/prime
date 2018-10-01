# -*- coding: utf-8 -*-

from random import randint
import math
import time
from functools import wraps

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

IS_PRIME_LTE7 = [False, False, True, True, False, True, False, True]

def miller_rabin(n, k=50):
    """
    Miller-Rabin Primality Test
    Returns true if n is a (probable) prime
    Returns false if n is a composite number
    """
    n = int(abs(n))
    if n <= 7:
        return IS_PRIME_LTE7[n]

    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        s = s + 1
        d = d >> 1
    for _ in range(k):
        a = randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            elif x == n - 1:
                a = 0
                break
        if a:
            return False
    return True

def rand_prime(bitsa, bitsb = None, k = 50):
    bitsa = int(abs(bitsa))
    bitsb = int(abs(bitsb)) if bitsb else bitsa

    if bitsa > bitsb:
        bitsa, bitsb = bitsb, bitsa
    elif bitsa == bitsb:
        bitsa = bitsb - 1

    lower = pow(2, bitsa)
    upper = pow(2, bitsb)
    upper_ = upper - upper / (int(math.log(upper)) + 1)
    r = lower + randint(0, upper_ - lower)
    r = r + 1 if r % 2 == 0 else r
    while 1:
        if miller_rabin(r, k):
            return r
        r += 2
        if r > upper:
            r = lower + randint(0, upper_ - lower)
            r = r + 1 if r % 2 == 0 else r

###########################################################################
###########################################################################
###########################################################################

def is_prime(n):
    n = int(abs(n))
    if n <= 7:
        return IS_PRIME_LTE7[n]

    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False

    for i in xrange(11, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


###########################################################################
###########################################################################
###########################################################################


def fn_timer(function):
  @wraps(function)
  def function_timer(*args, **kwargs):
    t0 = time.time()
    result = function(*args, **kwargs)
    t1 = time.time()
    print ("Total time running %s: %s seconds" %
        (function.func_name, str(t1-t0))
        )
    return result
  return function_timer

@fn_timer
def test1(num_list, k = 50):
    return [n for n in num_list if miller_rabin(n, k)]

@fn_timer
def test2(num_list):
    return [n for n in num_list if is_prime(n)]

@fn_timer
def test3(n):
    return rand_prime(n)

def main():
    n = 1024
    t = test3(n)
    assert miller_rabin(t) and t < pow(2, n) and t > pow(2, n - 1), "质数错误"
    print t

    base = 1000000000
    num = 100000
    num_list = [ n for n in range(base, base + num) if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0 ]
    ret1 = test1(num_list)
    print 'test1 OK'

    ret2 = test2(num_list)
    print 'test2 OK'

    assert len(ret1) == len(ret2), "素数个数不相同"
    assert ret1[-1] == ret2[-1], "素数 不相同"


if __name__ == '__main__':
    main()
