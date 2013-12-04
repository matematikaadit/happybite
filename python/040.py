# Champernowne's Constant
#
# If d_n represents the n-th digit of the fractional part, find the value
# of the following expression.
# d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
s = "0"
for i in range(1,1000000): s += str(i)
from operator import mul
from functools import reduce
print(reduce(mul,[int(s[10**i]) for i in range(7)]))
# output: 210
