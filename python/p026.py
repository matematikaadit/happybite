# Reciprocal Cycle
#
# Find the value of d < 1000 for which 1/d contains the longest recurring
# cycle in its decimal fraction part.

def recycle(n):
    pos = {}
    a = 1
    for i in range(n):
        if a in pos:
            return i - pos[a]
        if a == 0:
            return 0
        pos[a] = i
        a = (a*10) % n
    return 0

rest = 0
num = 0

for d in range(999,0,-1):
    if d <= rest: break

    c = recycle(d)
    if c > rest:
        rest, num = c, d

print(num)
# output: 983
