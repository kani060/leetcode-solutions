# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[float('inf')]*(amount+1) for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0]=0
        for i in range(1,amount+1):
            if i%coins[0]==0:
                dp[0][i]=i//coins[0]
        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                if j>=coins[i]:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-coins[i]]+1)
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[len(coins)-1][amount] if dp[len(coins)-1][amount]!=float('inf') else -1
