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

for i in range(len(abundant)):
    for j in range(i+1):
        n = abundant[i] + abundant[j]
        if n < largest:
            asum[abundant[i]+abundant[j]] = True

result = [n for n in range(largest) if not(asum[n])]
print(sum(result))
# output: 4179871
# TODO: find efficient algorithm
