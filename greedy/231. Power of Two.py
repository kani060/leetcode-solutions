# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.
# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        i = 0
        while 2 ** i <= n:
            if 2 ** i == n:
                return True
            i += 1
        return False
