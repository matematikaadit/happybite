# Path sum: two ways
#

with open('../sources/matrix.txt') as f:
    source = f.read()

mtx = [[int(n) for n in line.split(',')] for line in source.splitlines()]

for y in range(len(mtx)):
    for x in range(len(mtx[y])):
        if x == 0 and y == 0:
            continue
        if x == 0:
            mtx[y][x] += mtx[y-1][x]
        if y == 0:
            mtx[y][x] += mtx[y][x-1]
        if x != 0 and y != 0:
            # tambah minimal atas atau kiri
            mtx[y][x] += min(mtx[y-1][x],mtx[y][x-1])

print(mtx[-1][-1])