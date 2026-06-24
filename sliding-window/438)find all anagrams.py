# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l=[]
        k=len(p)
        s1=[0]*26
        s2=[0]*26
        if len(p)>len(s):
            return l
        for i in range(k):
            s1[ord(s[i])-ord("a")]+=1
            s2[ord(p[i])-ord("a")]+=1
        if s1==s2:
            l.append(0)
        for i in range(k,len(s)):
            s1[ord(s[i-k])-ord("a")]-=1
            s1[ord(s[i])-ord("a")]+=1
            if s1==s2:
                l.append(i-k+1)
        return l

            
