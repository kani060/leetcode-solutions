# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
# Example 1:
# Input: s = "IceCreAm"

# Output: "AceCreIm"
class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        s=list(s)
        while i<j:
            if s[i] in 'AEIOUaeiou' and s[j] in 'AEIOUaeiou':
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i] in 'AEIOUaeiou' and s[j] not in 'AEIOUaeiou':
                j-=1
            else:
                i+=1
        s="".join(s)
        return s
