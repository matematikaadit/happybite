# Maximum path sum II
#
# Find the maximum total from top to bottom in triangle.txt,
# a 15K text file containing a triangle with one-hundred rows.

with open("../sources/triangle.txt") as f:
    source = f.read()

grid = [[int(x) for x in row.split()] for row in source.splitlines()]

def update():
    for y in range(len(grid)-2,-1,-1):
        for x in range(len(grid[y])):
            grid[y][x] += max(grid[y+1][x],grid[y+1][x+1])

update()

print(grid[0][0])
# output: 7273
