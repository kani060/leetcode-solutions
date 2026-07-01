# In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

# Return the maximum amount of gold you can collect under the conditions:

# Every time you are located in a cell you will collect all the gold in that cell.
# From your position, you can walk one step to the left, right, up, or down.
# You can't visit the same cell more than once.
# Never visit a cell with 0 gold.
# You can start and stop collecting gold from any position in the grid that has some gold.
 

# Example 1:

# Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
# Output: 24
# Explanation:
# [[0,6,0],
#  [5,8,7],
#  [0,9,0]]
# Path to get the maximum gold, 9 -> 8 -> 7.

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = 0
        sol = [[0] * len(grid[0]) for _ in range(len(grid))]

        def f(i, j, c):
            nonlocal m

            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or sol[i][j] == 1 or grid[i][j] == 0:
                return

            sol[i][j] = 1
            c += grid[i][j]

            if c > m:
                m = c

            f(i + 1, j, c)
            f(i - 1, j, c)
            f(i, j + 1, c)
            f(i, j - 1, c)

            sol[i][j] = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    f(i, j, 0)

        return m
