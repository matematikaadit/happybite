# Digit factorials
#
# Find the sum of all numbers which are equal to the sum of the factorial of
# their digits.
from math import factorial
f = [ factorial(i) for i in range(10) ]
fsum = lambda n: sum(f[int(i)] for i in str(n))
result = sum( n for n in range(10,7*factorial(9)) if fsum(n) == n )
print(result)
# output: 40730
