# Pandigital products
#
# Find the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pandigital.

def combine(*arg):
    rest = ''
    for i in arg:
        rest += str(i)
    return sorted(rest)

from string import digits
def pandigital(a,b,c):
    s = combine(a,b,c)
    return s == list(digits[1:]) # without zero

rest = set()
for a in range(1,100):
    for b in range(100,10000):
        if a < 10 and b < 1000:
            continue
        if a > 9 and b > 999:
            continue
        c = a*b
        if pandigital(a,b,c):
            # print("{} x {} = {}".format(a,b,c))
            rest.add(c)

# print(rest)
print(sum(rest))
# output: 45228
