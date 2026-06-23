# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
# Example 1:
# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=[]
        max=0
        for i in range(len(accounts)):
            m.append(sum(accounts[i]))
        for ch in m:
            if ch>max:
                max=ch
        return max
