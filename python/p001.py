#!/usr/bin/env python3

# Multiples of 3 and 5
#
# Find the sum of all multiples of 3 or 5 below 1000
# NOTE: 1000 doesn't included in the summation

print(sum(x for x in range(1,1000) if x%3==0 or x%5==0))

# output: 233168
