# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.
# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        m=0
        l=0
        a=0
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
            m=max(m,d[s[i]])
            while (i-l+1)-m>k:
                d[s[l]]-=1
                l+=1
            a=max((i-l+1),a)
        return a
            
        
