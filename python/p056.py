# Powerful digit sum
#
# Considering natural numbers of the form, a^b, where a,b < 100,
# what is the maximum digital sum?

digitsum = lambda x: sum(int(c) for c in str(x))

r = max(digitsum(a**b) for a in range(1,100) for b in range(1,100))
print(r)
# output: 972
