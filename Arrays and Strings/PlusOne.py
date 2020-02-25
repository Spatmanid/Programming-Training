# Date 19/02/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/plus-one/
#
############### Plus One ###############
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a 
# single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 
# Example 2:
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#
# Complexity Analysis
# Time Complexity: O(n), where n is the length of digits.
# Space Complexity: O(1).

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while carry and i >= 0:
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            i -= 1
        if carry == 1:
            digits.insert(0, 1)
        return digits
        
def main():
    sol = Solution()
    digits = [1,2,3]
    print(sol.plusOne(digits))
    digits = [4,3,2,1]
    print(sol.plusOne(digits))
    
if __name__ == "__main__":
    main()
