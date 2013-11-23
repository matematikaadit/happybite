#!/usr/bin/env python3

# Summation of Primes
#
# Find the sum of all the primes below two million.

MAX = 2000000

primality = [True] * MAX

primality[0] = False
primality[1] = False

k = 2
while k*k < MAX:
    if primality[k]:
        for i in range(k*k,MAX,k):
            primality[i] = False
    k += 1

total = sum(x for x, verdict in enumerate(primality) if verdict)

print(total)

# output: 141676
