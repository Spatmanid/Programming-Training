# Date 02/04/2020
# @author Spyros Patmanidis
#
#
# References
# https://leetcode.com/problems/backspace-string-compare/
#
#
# ############### Happy Number ###############
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum
# of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in # a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 
# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            digits = [int(d) for d in str(n)]
            n = sum(d**2 for d in digits)
            if n == 1: return True
            if n in seen: return False
            seen.add(n)

def main():
    sol = Solution()
    n = 19
    print(sol.isHappy(n))

if __name__ == "__main__":
    main()
