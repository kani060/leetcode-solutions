# Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.

# A substring is a contiguous sequence of characters within a string.
# Example 1:

# Input: patterns = ["a","abc","bc","d"], word = "abc"
# Output: 3

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        c=0
        for ch in patterns:
            if ch in word:
                c+=1
        return c
