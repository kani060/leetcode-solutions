# You are given an m x n integer array grid where grid[i][j] could be:

# 1 representing the starting square. There is exactly one starting square.
# 2 representing the ending square. There is exactly one ending square.
# 0 representing empty squares we can walk over.
# -1 representing obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        m=len(grid)
        sol=[[0]*n for _ in range(m)]
        si,sj=0,0
        t=0
        a=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=-1:
                    t+=1
                if grid[i][j]==1:
                    si,sj=i,j
        def f(i,j,c):
            nonlocal a,t
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]==-1 or sol[i][j]==1:
                return False
            if grid[i][j]==2:
                if c==t:
                    a+=1
                return True
            sol[i][j]=1
            f(i+1,j,c+1)
            f(i-1,j,c+1)
            f(i,j+1,c+1)
            f(i,j-1,c+1)
            sol[i][j]=0
        f(si,sj,1)
        return a
