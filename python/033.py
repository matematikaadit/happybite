# Digit canceling fractions
#
# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator and
# denominator.
#
# If the product of these four fractions is given in its lowest common
# terms, find the value of the denominator.

def s(a,b):
    return 10*a+b

from fractions import Fraction
def cfrac(a,b,c):
    ab = s(a,b)
    ac = s(a,c)
    ba = s(b,a)
    ca = s(c,a)
    if ab < ca and Fraction(ab,ca) == Fraction(b,c):
        return Fraction(b,c)
    if ba < ac and Fraction(ba,ac) == Fraction(b,c):
        return Fraction(b,c)
    return None

result = []
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if cfrac(a,b,c): result.append(cfrac(a,b,c))

from operator import mul
from functools import reduce

r = reduce(mul, result)
print(r.denominator)
# output: 100
