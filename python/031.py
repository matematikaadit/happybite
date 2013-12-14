# Coin sums
#
# In England the currency is made up of pound, £, and pence, p, and
# there are eight coins in general circulation:
#
#   1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#
# How many different ways can £2 be made using any number of coins?

a = (1,2,5,10,20,50,100,200)

def f(n,k):
    if n < 0 or k < 0:
        return 0
    if n == 0:
        return 1
    return f(n,k-1) + f(n-a[k],k)

print(f(200,len(a)-1))

# output: 73682
