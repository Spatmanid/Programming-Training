# Date 09/11/2019
# @author Spyros Patmanidis
#
#
# References
# https://leetcode.com/problems/two-sum/
#
#
# Two Sum
# Easy
# You are given an array of integers. You are asked to return the indices of the two numbers
# such that they add up to a specific target. You may assume that each input would have exaclty
# one solution, and may not use the same element twice.
#
# Examples
#
# Input: nums = [1, 3, 10, 7, 2], target = 5
# Output: [1, 4]
# Explanation: nums[1] + nums[4] = 3 + 2 = 5
#
# Solution
#
# In this problem, we have an unordered list of integers. If the list was ordered, we could find
# the required indices in O(n) time and O(1) space, where n is the number of elements in nums. We
# can still solve the problem in O(n) time if we use a hashtable. However, in that case the space
# complexity is O(n). If we wanted the complexity to be O(1), we can sort nums and use the two pointers
# approach, which however has a time complexity of O(n logn).
# 
# Complexity Analysis
# This solution has time and space complexity of O(n).

class Solution:
    def twoSum(self, nums, target):
        if len(nums) < 1:
            return []
        h = {}
        for i, num in enumerate(nums):
            if target - num in h:
                return [h[target - num], i]
            h[num] = i
        return []
        

def main():
    sol = Solution()
    nums = [1, 3, 10, 7, 2]
    target = 5
    print(sol.twoSum(nums, target))

if __name__ == "__main__":
    main()
