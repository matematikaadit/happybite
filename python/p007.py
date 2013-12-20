#!/usr/bin/env python3

# 10001st Prime
#
# What is the 10001st prime number?

import primes

# n-th primes always less than
# n*(ln(n)+ln(ln(n)))
# for all n >= 6
# see:
# http://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number

from math import log # ln is log in math

k = 10000
limit = int(k * (log(k) + log(log(k))))

ps = primes.gen(limit)

print(ps[k])

# output: 104743
