# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
 j=0
        for i in range(len(nums)):
           if nums[i]!=0:
               nums[i],nums[j]=nums[j],nums[i]
               j+=1
        return numsclass Solution:
   
