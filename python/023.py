# Non-abundant sums
#
# Find the sum of all the positive integers which cannot be written as the
# sum of two abundant numbers.


largest = 28123 + 1
d = [0 for _ in range(largest)]

for n in range(1,largest):
    for k in range(2*n,largest,n):
        d[k] += n

abundant = [ n for n in range(largest) if d[n] > n ]

asum = [False for _ in range(largest)]

from itertools import combinations_with_replacement
s = combinations_with_replacement(abundant, 2)
for i, j in s:
    if i+j < largest: asum[i+j] = True

result = [n for n in range(largest) if not(asum[n])]
print(sum(result))
# output: 4179871
# TODO: find efficient algorithm
