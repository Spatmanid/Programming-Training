# Date 03/04/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/target-sum/
#
############### Target Sum ###############
#  You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each
# integer, you should choose one from + and - as its new symbol.
# Find out how many ways to assign symbols to make sum of integers equal to target S.
# 
# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 
#   -1+1+1+1+1 = 3
#   +1-1+1+1+1 = 3
#   +1+1-1+1+1 = 3
#   +1+1+1-1+1 = 3
#   +1+1+1+1-1 = 3
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# 
# Note:
# 
#     The length of the given array is positive and will not exceed 20.
#     The sum of elements in the given array will not exceed 1000.
#     Your output answer is guaranteed to be fitted in a 32-bit integer.
#
# Complexity Analysis
# Time: O(N * T), where N = # of items and T is the target sum(arr) - S.
# Space: O(N).

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        target = sum(nums) - S
        if target < 0 or target % 2: return 0
        target //= 2
        dp = [1] + [0] * target
        for num in nums:
            for j in range(num, target+1)[::-1]:
                dp[j] += dp[j - num]
        return dp[target]
        
def main():
    sol = Solution()
    nums, S = [1, 1, 1, 1, 1], 3
    print(sol.findTargetSumWays(nums, S))
    
if __name__ == "__main__":
    main()
