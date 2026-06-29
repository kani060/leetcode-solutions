# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Example 1:

# Input: s = "()"

# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        b=True
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack:
                     b=False
                     break
                top=stack.pop()
                if (ch==')' and top!='(') or (ch==']' and top!='[') or (ch=='}' and top!='{'):
                    b=False
                    break
        if stack:
            b=False
        return b
