# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
class Solution:
    def reverseString(self, s: List[str]) -> None:
        i=0
        j=len(s)-1
        while i<len(s)//2 and j>=0:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return s
        
