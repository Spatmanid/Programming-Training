# Date 26/02/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/trapping-rain-water/
#
############### Trapping Rain Water ###############
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is
# able to trap after raining.
#
# Example:
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#
# Solution using 2 pointers:
# Initialize left pointer to 0 and right pointer to len(height) - 1
# Keep track of the left max height and right max height
# Iterate the array
# if l_max <= r_max update and increase the left pointer, else update and decrease right pointer.
#
# Complexity Analysis
# Time Complexity: O(N).
# Space Complexity: O(1).

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3: return 0
        l, r = 0, len(height) - 1
        l_max, r_max, water = height[l], height[r], 0
        while l < r:
            if l_max <= r_max:
                water += l_max - height[l]
                l += 1
                l_max = max(l_max, height[l])
            else:
                water += r_max - height[r]
                r -= 1
                r_max = max(r_max, height[r])
        return water
        
def main():
    sol = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(sol.trap(height))
    
if __name__ == "__main__":
    main()
