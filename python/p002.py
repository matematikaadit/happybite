#!/usr/bin/env python3

# Even Fibonacci numbers
#
# find the sum of even-valued terms of fibonacci numbers whose value
# doesn't exceed four million

a = 1
b = 1
total = 0
MAX = 4000000

while a < MAX:
    if a%2==0:
        total += a
    a, b = b, a+b

print(total)

# output: 4613732
