# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        dp=[[0]*m for _ in range(n)]
        for i in range(m):
            dp[0][i]=matrix[0][i]
        for i in range(1,n):
            for j in range(m):
                up = dp[i - 1][j]
                if j > 0:
                    left = dp[i - 1][j - 1]
                else:
                    left=float('inf')
                if j < n - 1:
                    right = dp[i - 1][j + 1] 
                else:
                    right=float('inf')

                dp[i][j] = matrix[i][j] + min(up, left, right)
        return min(dp[-1])
