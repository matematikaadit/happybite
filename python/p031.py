# Coin sums
#
# In England the currency is made up of pound, £, and pence, p, and
# there are eight coins in general circulation:
#
#   1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#
# How many different ways can £2 be made using any number of coins?

a = (1,2,5,10,20,50,100,200)

t = [[0 for _ in range(len(a))] for _ in range(201)]

for n in range(len(t)):
    for k in range(len(t[n])):
        if n == 0 or k == 0:
            t[n][k] = 1
        elif n - a[k] < 0:
            t[n][k] = t[n][k-1]
        else:
            t[n][k] = t[n][k-1] + t[n-a[k]][k]

print(t[200][-1])

# output: 73682
