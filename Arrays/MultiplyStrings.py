# Date 19/02/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/multiply-strings/
#
############### Multiply Strings ###############
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as # a string.
# 
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
# 
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
# Note:
#     The length of both num1 and num2 is < 110.
#     Both num1 and num2 contain only digits 0-9.
#     Both num1 and num2 do not contain any leading zero, except the number 0 itself.
#     You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
# Complexity Analysis
# Time Complexity: O(m * n), where m is the length of num1 and n is the length of num2.
# Space Complexity: O(m + n).

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) == '0' or len(num2) == '0': return '0'
        product = [0] * (len(num1) + len(num2))
        position = len(product) - 1
        for n1 in num1[::-1]:
            tempPos = position
            for n2 in num2[::-1]:
                product[tempPos] += (ord(n1) - ord('0')) * (ord(n2) - ord('0'))
                product[tempPos - 1] += product[tempPos] // 10
                product[tempPos] %= 10
                tempPos -= 1
            position -= 1
        pointer = 0
        while pointer < len(product) - 1 and product[pointer] == 0:
            pointer += 1
        return ''.join(map(str, product[pointer:]))
            
def main():
    sol = Solution()
    num1, num2 = '2', '3'
    print(sol.multiply(num1, num2))
    num1, num2 = '123', '456'
    print(sol.multiply(num1, num2))
    
if __name__ == "__main__":
    main()
