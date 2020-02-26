# Date 26/02/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/valid-parentheses/
#
############### Valid Parenthesis ###############
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
# 
# Example 1:
# Input: "()"
# Output: true
# 
# Example 2:
# Input: "()[]{}"
# Output: true
# 
# Example 3:
# Input: "(]"
# Output: false
# 
# Example 4:
# Input: "([)]"
# Output: false
#
# Example 5:
# Input: "{[]}"
# Output: true
#
# Complexity Analysis
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2: return False
        valid = { ')':'(', '}':'{', ']':'[' }
        stack = []
        for c in s:
            if c in valid.values():
                stack.append(c)
            elif c in valid.keys():
                if not stack or valid[c] != stack.pop():
                    return False
            else:
                return False
        return stack == []
        
def main():
    sol = Solution()
    s = "()"
    print(sol.isValid(s))
    s = "()[]{}"
    print(sol.isValid(s))
    s = "(]"
    print(sol.isValid(s))
    s = "([)]"
    print(sol.isValid(s))
    s = "{[]}"
    print(sol.isValid(s))
    
if __name__ == "__main__":
    main()
