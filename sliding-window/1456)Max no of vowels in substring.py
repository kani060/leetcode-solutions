# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ma=0
        c=0
        v='aeiou'
        for i in range(k):
            if s[i] in v:
                c+=1
        ma=c
        for i in range(k,len(s)):
            if s[i-k] in v:
                c-=1
            if s[i] in v:
                c+=1
            ma=max(ma,c)
        return ma
