# Date 25/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/score-of-parentheses/
#
############### Score of Parentheses ###############
# Given a balanced parentheses string S, compute the score of the string based on the following rule:
#    () has score 1
#    AB has score A + B, where A and B are balanced parentheses strings.
#    (A) has score 2 * A, where A is a balanced parentheses string.
#
# Example 1:
# Input: "()"
# Output: 1
#
# Example 2:
# Input: "(())"
# Output: 2
#
# Example 3:
# Input: "()()"
# Output: 2
# Example 4:
# Input: "(()(()))"
# Output: 6
#
# Complexity Analysis
# Time Complexity: O(n), where n the length of S.
# Space Complexity: O(n).

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        for c in S:
            if c == '(':
                stack.append(0)
            else:
                score = stack.pop()
                stack[-1] += max(2 * score, 1)
        return stack.pop()
        
def main():
    sol = Solution()
    S = "()"
    print(sol.scoreOfParentheses(S))
    S = "(())"
    print(sol.scoreOfParentheses(S))
    S = "()()"
    print(sol.scoreOfParentheses(S))
    S = "(()(()))"
    print(sol.scoreOfParentheses(S))
    
if __name__ == "__main__":
    main()
