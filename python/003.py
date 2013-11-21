#!/usr/bin/env python3

# Largest prime factor
#
# What is the largest prime factor of the number 600851475143

n = 600851475143
k = 2
last = k

while n > 1:
    if n%k==0:
        last = k
        while n%k==0:
            n /= k
    k += 1

print(last)

# output: 6857
