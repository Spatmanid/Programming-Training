# Date 25/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/generate-parentheses/
#
############### Generate Parentheses ###############
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# For example, given n = 3, a solution set is:
# ["((()))", "(()())", "(())()", "()(())", "()()()"]
#
# Complexity Analysis
# Time Complexity: O(4^n / sqrt(n)).
# Space Complexity: O(4^n / sqrt(n)).

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(left, right, current):
            if left == 0 and right == 0:
                result.append(current)
                return
            if left > 0:
                backtrack(left-1, right, current + '(')
            if right > left:
                backtrack(left, right-1, current + ')')
        result = []
        backtrack(n, n, '')
        return result
        
def main():
    sol = Solution()
    print(sol.generateParenthesis(3))
    
if __name__ == "__main__":
    main()
