# Quadratic primes
#
# Considering quadratics of the form:
#
#     n² + an + b, where |a| < 1000 and |b| < 1000
#
# Find the product of the coefficients, a and b, for the quadratic
# expression that produces the maximum number of primes for
# consecutive values of n, starting with n = 0.

# When n = 0, p(0) = b, hence b prime

import primes
p = primes.gen(1000)
pc = primes.gen(p[-1]**2+1000*p[-1]+p[-1])

def not_prime(n):
    for m in pc:
        if n == m:
            return False
        if n < m:
            return True
    return True

def strike(a,b):
    for n in range(b):
        fn = n*n + a*n + b
        if not_prime(fn):
            return n
    return b

ma, mb, mn = 0, 0, 0

for a in range(-999,1000,2):
    for b in p:
        n = strike(a,b)
        if n > mn:
            ma, mb, mn = a, b, n

print(ma*mb)
# output: -59231
