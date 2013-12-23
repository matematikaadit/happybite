# Longest Collatz sequence
#
# Which starting number, under one million, produces the longest chain?

collatz = {1: 1, 2: 2}

def collatz_chain(number):
    if number in collatz:
        return collatz[number]

    k = 1
    if number % 2 == 0:
        k = 1 + collatz_chain(number//2)
    else:
        k = 1 + collatz_chain(3*number+1)
    collatz[number] = k
    return k

longest = [1, 1]
for i in range(1,1000000):
    c = collatz_chain(i)
    if c > longest[1]:
        longest = [i, c]

print(longest)

# output: [837799, 525]
# TODO: buat lebih efisien
