# 9)Given an integer x, return true if x is a palindrome, and false otherwise.
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        if str(x)==s[::-1]:
            return True
        else:
            return False
# 1)Two sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
  a=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    a.append(i)
                    a.append(j)
                    break
        return a
# Contains duplicate-Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
   x=set(nums)
        if len(x)==len(nums):
            return False
        else:
            return True
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# Example 1:
# Input: nums = [2,2,1]
# Output: 1
 ans=0
       for ch in nums:
          ans^=ch
       return ans  
# movezeros-Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
 def moveZeroes(self, nums: List[int]) -> None:
        j=0
        for i in range(len(nums)):
           if nums[i]!=0:
               nums[i],nums[j]=nums[j],nums[i]
               j+=1
        return nums
