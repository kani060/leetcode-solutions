# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        ma=0
        c=0
        for i in range(len(nums)):
            if nums[i]==0:
                c+=1
            while c>1:
                if nums[l]==0:
                    c-=1
                l+=1
            ma=max(ma,i-l)
        return ma
