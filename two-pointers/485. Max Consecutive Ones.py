# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        y=[]
        s=0
        for ch in nums:
            if ch!=0:
                s+=ch
            else:
                y.append(s)
                s=0
        y.append(s)
