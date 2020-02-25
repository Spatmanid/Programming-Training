# Date 12/11/2019
# @author Spyros Patmanidis
#
#
# References
# https://leetcode.com/problems/container-with-most-water/
#
#
# Container With Most Water
# Medium
# You are given n non-negative integers a_1, a_2, ..., a_n, where each element represents 
# a point at cordinate (i, a_i). n vertical lines are drawn such that the two endpoints of
# i is at (i, a_i) and (i, 0). Find two lines, which together with x-axis form a container
# such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
# Examples
#
# Input: nums = [1,8,6,2,5,4,8,3,7]
# Output: 49
#
# Solution
#
# In this problem, the brute force solution is to enumerate all possible containers and
# return the container with the maximum area. However, this solution has time complexity of
# O(n^2). We can use the two pointers method to reduce the time complexity to O(n). At each
# iteration we move the pointer where the height is lower.
# 
# Complexity Analysis
# As mentioned earlier the time complexity is O(n) and the space complexity is O(1).

class Solution:
    def maxArea(self, height):
        low, high = 0, len(height) - 1
        maxArea = 0
        
        while low < high:
            if height[low] <= height[high]:
                maxArea = max(maxArea, height[low] * (high - low))
                low += 1
            else:
                maxArea = max(maxArea, height[high] * (high - low))
                high -= 1
        return maxArea
        
def main():
    height = [1,8,6,2,5,4,8,3,7]
    sol = Solution()
    print(sol.maxArea(height))
    
if __name__ == "__main__":
    main()
