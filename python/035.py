# Circular primes
#
# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
# 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

import primes

prime_list = primes.gen(1000000)

def cycle(m):
    s = str(m)
    n = s[1:]+s[:1]
    rest = [s]
    while n != s:
        rest.append(n)
        n = n[1:] + n[:1]
    return rest

def circular_prime(p):
    cs = cycle(p)
    if '0' in cs[0]: return False
    return all(int(c) in prime_list for c in cs)

rest = [p for p in prime_list if circular_prime(p)]
print(len(rest))
# output: 55
# TODO: improve the execution time
