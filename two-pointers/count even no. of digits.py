# Given an array nums of integers, return how many of them contain an even number of digits.
# Example 1:
# Input: nums = [12,345,2,6,7896]
# Output: 2
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n=0
        for ch in nums:
            x=str(ch)
            if len(x)%2==0:
                n+=1
        return n
