# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
x=[]
        sum=0
        for ch in nums:
            sum+=ch
            x.append(sum)
        return x
