# Date 02/04/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/maximum-subarray/
#
############### Maximum Subarray ###############
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and 
# return its sum.
#
# Example:
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# Complexity Analysis
# Time: O(n), where n = len(nums).
# Space: O(1).

class Solution:
    def def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = nums[0]
        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            maxSum = max(maxSum, nums[i])
        return maxSum
        
def main():
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(sol.maxSubArray(nums))
    
if __name__ == "__main__":
    main()
