# Digit fifth powers
#
# Find the sum of all the numbers that can be written as the sum of fifth
# powers of their digits.
def digitsum(n,p):
    result = 0
    while n > 0:
        result += (n%10)**p
        n //=10
    return result

# maximum for 6 digit is 6 * 9**5 = 354294 less than 999999
print(sum(n for n in range(10,6*9**5) if n == digitsum(n,5)))
# output: 443839
