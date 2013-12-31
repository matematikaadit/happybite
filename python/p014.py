# Longest Collatz sequence
#
# Which starting number, under one million, produces the longest chain?

collist = [0]*1000000

def collatz(n):
    orin = n
    count = 0

    while n >= orin:
        if n % 2 == 0:
            count += 1
            n //= 2
        else:
            count += 1
            n = n*3+1
    collist[orin] = count + collist[n]
    return collist[orin]

a = [1, 1]
collist[1] = 1
for i in range(2,1000000):
    c = collatz(i)
    if c > a[1]:
        a = [i, c]

print(a)

# output: [837799, 525]
# TODO: buat lebih efisien
