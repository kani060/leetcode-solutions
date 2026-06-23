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
