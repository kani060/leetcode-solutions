# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.
# Example 1:

# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for ch in words:
            if ch==ch[::-1]:
                return ch
        else:
            return ""
