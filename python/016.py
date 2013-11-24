# Power digit sum
#
# What is the sum of the digits of the number 2^1000

def dsum(n):
    if n < 10: return n
    else: return n%10 + dsum(n//10)

print(dsum(2**1000))

# output: 1366
# TODO: print(sum(int(n) for n in str(2**1000)))
