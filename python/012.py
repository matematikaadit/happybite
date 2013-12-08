# Highly divisible triangular number
#
# What is the value of the first triangular number to have over five hundred
# divisors?

def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def triangles():
    n = 1
    while True:
        yield (n+1) * n // 2
        n += 1

pl = primes(2000000)

def d(n):
    rest = 1
    for i in pl:
        e = 1
        if i * i > n:
            rest *= 2
            break
        while n % i == 0:
            e += 1
            n //= i
        rest *= e
        if n == 1: break
    return rest

def solve():
    for i in triangles():
        last = d(i)
        if last >= 500:
            print(i)
            break

solve()

# output: 76576500
# TODO: consider using more efficient method
# BEFORE: 25.6 s
# AFTER: 1.6 s
