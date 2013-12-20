# Lattice paths
#
# How many such routes are there through a 20x20 grid?

lat = {}
def lattice(m,n):
    if m > n:
        return lattice(n,m)

    if (m, n) in lat:
        return lat[(m,n)]

    if m == 0:
        k = 1
    else:
        k = lattice(m,n-1) + lattice(m-1,n)

    lat[(m,n)] = k
    return k

print(lattice(20,20))

# output: 137846528820
