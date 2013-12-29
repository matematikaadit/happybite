# Number spiral diagonals
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?
def spiral(n):
    s = 1
    for i in range(3,n+1,2):
        s += 4*i*i - 6*(i-1) # by finding the pattern
    return s

print(spiral(1001))
# output: 669171001
