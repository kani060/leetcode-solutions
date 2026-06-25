# Given a string s, find the length of the longest substring without duplicate characters.
# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

  class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        z=[]
        r,c=0,0
        ma=0
        for i in range(len(s)):
            while s[r] in z:
                z.remove(s[c])
                c+=1
            z.append(s[r])
            r+=1
            ma=max(ma,len(z))
        return ma

