# Highly divisible triangular number
#
# What is the value of the first triangular number to have over five hundred
# divisors?

def triangles():
    n = 1
    while True:
        yield (n+1) * n // 2
        n += 1

import primes
pl = primes.gen(65536)

def d(n):
    rest = 1
    for i in pl:
        if n == 1: break
        if i * i > n:
            rest *= 2
            break
        if n % i == 0:
            e = 1
            while n % i == 0:
                e += 1
                n //= i
            rest *= e
    return rest

def solve():
    for i in triangles():
        last = d(i)
        if last >= 500:
            print(i)
            break

solve()

# output: 76576500
# TODO: consider using more efficient method
# BEFORE: 25.6 s
# AFTER: 1.01 s
