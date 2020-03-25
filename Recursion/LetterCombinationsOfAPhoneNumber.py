# Date 25/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#
############### Letter Combinations of a Phone Number ###############
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# Note that 1 does not map to any letters.
#
# Example:
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
# Complexity Analysis
# Time Complexity: O(4^n).
# Space Complexity: O(n).

class Solution:
    def letterCombinations(self, digits: str):
        if not digits: return []
        def dfs(current):
            if len(current) == len(digits):
                result.append(current)
                return
            for c in dic[digits[len(current)]]:
                dfs(current + c)
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = []
        dfs('')
        return result
        
def main():
    sol = Solution()
    digits = "23"
    print(sol.letterCombinations(digits))
    
if __name__ == "__main__":
    main()
