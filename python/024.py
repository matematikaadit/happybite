# Lexicographic permutations
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
# 4, 5, 6, 7, 8 and 9?

ns = list(range(10))
result = ""

x = 999999 # millionth lexicographic permutation

from math import factorial
for n in range(9,-1,-1):
    q = x // factorial(n)
    x = x % factorial(n)
    result += str(ns[q])
    del ns[q]

print(result)
# output: 2783915460
