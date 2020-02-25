# Date 12/11/2019
# @author Spyros Patmanidis
#
#
# References
# https://leetcode.com/problems/jump-game/
#
#
# Jump Game
# Medium
# You are given an array of non-negative integers. You are initially positioned at the
# first index of the array. Each element in the array represents your maximum jump length
# at that position. Determine if you are able to reach the last index.
#
# Examples
#
# Input: nums = [2,3,1,1,4]
# Output: True
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Input: nums = [3,2,1,0,4]
# Output: False
# Explantion: You will always arrive at index 3 no matter what. Its maximum jump length is 0, 
#             which makes it impossible to reach the last index.
#
# Solution
#
# In this problem, the brute force approach to this problem is to start from the first element
# and recursively call for all the elements reachable from the first one. The complexity of this
# solution is O(2^n). We can use a bottom-up or a top-down dynamic programming approach in order
# to reduce the time complexity to O(n^2). Yet, can achieve a time complexity of O(n) if we use a
# greedy method to solve this problem. We keep track of the maxJump we can achieve, we traverse the
# array in a linear way, and at each iteration we update the maxJump. If we reach an index greater
# than the maxJump that means that there is no way to reach this index with a jump from a previoys
# index and as a result we return False. If we reach the last index we return True.
# 
# Complexity Analysis
# As mentioned earlier the time complexity is O(n) and the space complexity is O(1).

class Solution:
    def canJump(self, nums):
        maxJump = i = 0
        while i <= maxJump and i < len(nums):
            maxJump = max(maxJump, i + nums[i])
            i += 1
        return i == len(nums)
        
def main():
    nums = [2,3,1,1,4]
    sol = Solution()
    print(sol.canJump(nums))
    nums = [3,2,1,0,4]
    print(sol.canJump(nums))
    
if __name__ == "__main__":
    main()
