import numpy as np
import re

# input = np.loadtxt('d2.txt', dtype=int)
input = open("d4.txt","r")

grid = []

for line in input:
    if line[-1] == "\n":
        grid.append(list(line)[:-1])#
    else:  
        grid.append(list(line))

ilen = len(grid)
jlen = len(grid[0])

count = 0
part = 2

if part == 1:
    for i in range(ilen):
        for j in range(jlen):
            # Forward 
            if i + 3 < ilen:
                if grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+3][j] == "XMAS":
                    count += 1
            # Backward
            if i - 3 >= 0:
                if grid[i][j] + grid[i-1][j] + grid[i-2][j] + grid[i-3][j] == "XMAS":
                    count += 1
            # Downward
            if j + 3 < jlen:
                if grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i][j+3] == "XMAS":
                    count += 1
            # Upward
            if j - 3 >= 0:
                if grid[i][j] + grid[i][j-1] + grid[i][j-2] + grid[i][j-3] == "XMAS":
                    count += 1
            # Diagonal Downward
            if i + 3 < ilen and j + 3 < jlen:
                if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] + grid[i+3][j+3] == "XMAS":
                    count += 1
            # Diagonal Upward
            if i - 3 >= 0 and j - 3 >= 0:
                if grid[i][j] + grid[i-1][j-1] + grid[i-2][j-2] + grid[i-3][j-3] == "XMAS":
                    count += 1
            # Diagonal Downward
            if i + 3 < ilen and j - 3 >= 0:
                if grid[i][j] + grid[i+1][j-1] + grid[i+2][j-2] + grid[i+3][j-3] == "XMAS":
                    count += 1
            # Diagonal Upward
            if i - 3 >= 0 and j + 3 < jlen:
                if grid[i][j] + grid[i-1][j+1] + grid[i-2][j+2] + grid[i-3][j+3] == "XMAS":
                    count += 1
else:
    for i in range(1, ilen-1):
        for j in range(1, jlen-1):
            # Check for cross pattern
            if grid[i][j] == 'A':
                if grid[i-1][j-1] == 'M' and grid[i+1][j+1] == 'S' and grid[i+1][j-1] == 'M' and grid[i-1][j+1] == 'S':
                    count += 1
                if grid[i-1][j-1] == 'S' and grid[i+1][j+1] == 'M' and grid[i+1][j-1] == 'S' and grid[i-1][j+1] == 'M':
                    count += 1
                if grid[i-1][j-1] == 'M' and grid[i+1][j+1] == 'S' and grid[i+1][j-1] == 'S' and grid[i-1][j+1] == 'M':
                    count += 1
                if grid[i-1][j-1] == 'S' and grid[i+1][j+1] == 'M' and grid[i+1][j-1] == 'M' and grid[i-1][j+1] == 'S':
                    count += 1

print(count)