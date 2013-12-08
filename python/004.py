#!/usr/bin/env python3

# Largest palindrome product
#
# Find the largest palindrome made from the product
# of two 3-digit numbers

def reverse(num):
    ret = 0
    while num > 0:
        ret = ret * 10 + num % 10
        num //= 10
    return ret

def palindrome(n):
    return n == reverse(n)

def largest():
    last = 0
    # Just check from 900, since lower than that
    # wont give us the largest palindrome number
    for x in range(900,1000):
        for y in range(900,1000):
            n = x * y
            if n > last and palindrome(n):
                last = n
    return last

print(largest())