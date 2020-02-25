# Date 09/11/2019
# @author Spyros Patmanidis
#
#
# References
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#
#
# Two Sum II - Input array is sorted
# Easy
# You are given an array of integers  that is already sorted in ascending order. You are asked
# to return the indices of the two numbers such that they add up to a specific target. 
# The function twoSum should return indices of the two numbers such that they add up to the target,
# where index1 must be less than index2. If there are no such integers, return [-1, -1]
#
# Examples
#
# Input: nums = [1, 2, 3, 7, 13, 18], target = 10
# Output: [2, 3]
# Explanation: nums[2] + nums[3] = 3 + 7 = 10
#
# Solution
#
# Since the array nums is sorted, we can use to pointers (low, high) to traverse the array. The low
# pointer will start from the first element of the array, while the high pointer will start from the
# the last element. At each iteration, if the sum of the two elements we examine is less than the
# target we will decrease the high pointer and if the sum of these two elements is greater that the
# target we will increase the low pointer. If the sum is equal the target we return the indexes.
# 
# Complexity Analysis
# This solution has time complexity of O(n), where n is the number of elements in the array nums,
# and space complexity of O(1).

class Solution:
    def twoSum(self, nums, target):
        low, high = 0, len(nums) - 1
        while low < high:
            if nums[low] + nums[high] == target:
                return [low, high]
            elif nums[low] + nums[high] < target:
                low += 1
            else:
                high -= 1
        return [-1, -1]
        
def main():
    nums = [1, 2, 3, 7, 13, 18]
    target = 10
    sol = Solution()
    print(sol.twoSum(nums, target))
    
if __name__ == "__main__":
    main()    
