# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
# Example 1:

# Input: s = "loveleetcode", c = "e"
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        y=[]
        for i in range(len(s)):
            if s[i]==c:
                y.append(i)
        o=[]
        for i in range(len(s)):
            z=[]
            for j in range(len(y)):
                z.append(abs(i-y[j]))
            o.append(min(z))
        return o
