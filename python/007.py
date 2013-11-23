#!/usr/bin/env python3

# 10001st Prime
#
# What is the 10001st prime number?

# naive method

primes = [2,3,5,7,11]

def prime(n):
    for p in primes:
        if n % p == 0:
            return False
    return True

k = 5  # 5 bilangan prima sudah kita daftar di dalam primes
n = 13 # bilangan selanjutnya yang di cek

while k < 10001:
    if prime(n):
        primes.append(n)
        k += 1
    n += 2


print(primes[-1])

# output: 104743
