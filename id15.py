"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

def velivelislowexplore(i, j, total):
    if i==20 and j==20:
        return 1
    elif i>20 or j>20:
        return 0
    else:
        return velivelislowexplore(i+1, j, total) + velivelislowexplore(i, j+1, total)

def fastExplore(n):
    lst = [[0]*n for x in range(n)]
    for i in range(n):
        lst[i][0], lst[0][i] = 1, 1
    for i in range(1, n):
        for j in range(1, n):
            lst[i][j] = lst[i-1][j] + lst[i][j-1]
    return lst[n-1][n-1]

print(fastExplore(21))