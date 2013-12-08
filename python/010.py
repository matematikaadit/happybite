#!/usr/bin/env python3

# Summation of Primes
#
# Find the sum of all the primes below two million.

def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

print(sum(primes(2000000)))
# output: 142913828922
