# Maximum path sum I
#
# find the maximum total from top to bottom of the triangle below:

with open("../sources/p018.txt") as f:
    source = f.read().strip()

grid = [[int(x) for x in row.split()] for row in source.splitlines()]

def max_path(y, x):
    if y < len(grid) - 1:
        return grid[y][x] + max(max_path(y+1,x), max_path(y+1,x+1))
    else:
        return grid[y][x]

print(max_path(0,0))

# output: 1074
