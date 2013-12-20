# Amicable numbers
#
# Evaluate the sum of all amicable numbers under 10000.

amicables = (220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368)
# see: http://oeis.org/A063990

largest = 10001
d = [0 for _ in range(largest)]

for n in range(1,largest):
    for k in range(2*n,largest,n):
        d[k] += n

ami = [n for n in range(largest) if
         d[n] < largest and d[n] != n and d[d[n]] == n ]
print(sum(ami))

# output: 31626
