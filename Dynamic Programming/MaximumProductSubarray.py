# Date 02/04/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/maximum-product-subarray/
#
############### Maximum Product Subarray ###############
# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the 
# largest product.
# 
# Example 1:
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# Example 2:
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
# Complexity Analysis
# Time: O(n), where n = len(nums).
# Space: O(1).

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        product = maxProdLeft= nums[0]
        for num in nums[1:]:
            if product == 0:
                product = num
            else:
                product *= num
            maxProdLeft = max(maxProdLeft, product)
        product = maxProdRight = nums[-1]
        for num in nums[:-1][::-1]:
            if product == 0:
                product = num
            else:
                product *= num
            maxProdRight = max(maxProdRight, product)
        return max(maxProdLeft, maxProdRight)
      
def main():
    sol = Solution()
    nums = [2,3,-2,4]
    print(sol.maxProduct(nums))
    nums = [-2, 0, -1]
    print(sol.maxProduct(nums))
    
if __name__ == "__main__":
    main()
