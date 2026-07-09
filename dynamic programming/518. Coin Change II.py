# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The final answer is guaranteed to fit into a signed 32-bit integer

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[[0]*(amount+1) for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0]=1
        for j in range(1,amount+1):
            if j%coins[0]==0:
                dp[0][j]=1
        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                if j>=coins[i]:
                    dp[i][j]=dp[i-1][j]+dp[i][j-coins[i]]
                else:
                    dp[i][j]+=dp[i-1][j]
        return dp[len(coins)-1][amount] 
