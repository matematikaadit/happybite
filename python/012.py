# Highly divisible triangular number
#
# What is the value of the first triangular number to have over five hundred
# divisors?

divisor = 1
n = 1
number = 0

def num_of_divisor(number):
    d = 1
    k = 2

    while number > 1:
        if number % k == 0:
            p = 0
            while number % k == 0:
                p += 1
                number //= k
            d *= (p+1)
        k += 1

    return d

while divisor <= 500:
    number += n
    n += 1
    divisor = num_of_divisor(number)
    # if divisor > 300: print(number,divisor)

print(number)

# output: 76576500
# TODO: consider using more efficient method
