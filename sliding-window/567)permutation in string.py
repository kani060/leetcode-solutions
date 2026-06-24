# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.
# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        s1c=[0]*26
        s2c=[0]*26
        if len(s1)>len(s2):
            return False
        for i in range(k):
            s1c[ord(s1[i])-ord("a")]+=1
            s2c[ord(s2[i])-ord("a")]+=1
        for i in range(k,len(s2)):
            if s1c==s2c:
                return True
            s2c[ord(s2[i-k])-ord("a")]-=1
            s2c[ord(s2[i])-ord("a")]+=1
        return s1c==s2c
