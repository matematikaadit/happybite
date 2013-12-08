#!/usr/bin/env python3

# Smallest Multiple
#
# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?

from fractions import gcd

res = 1

def lcd(a, b):
    return a * b // gcd(a, b)

for i in range(1, 21):
    res = lcd(res, i)

print(res)

# output: 232792560