# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

 class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        x=word.upper()
        y=word[0].upper()+word[1:].lower()
        z=word.lower()
        if word==x or word==y or word==z:
            return True
        else:
            return False
