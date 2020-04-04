# Date 04/04/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/move-zeroes/
#
############### Move Zeroes ###############
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero 
# elements.
# 
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
#     You must do this in-place without making a copy of the array.
#     Minimize the total number of operations.
#
# Complexity Analysis
# Time: O(n).
# Space: O(1).

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
def main():
    sol = Solution()
    nums = [0,1,0,3,12]
    sol.moveZeroes(nums)
    print(nums)
    
if __name__ == "__main__":
    main()
