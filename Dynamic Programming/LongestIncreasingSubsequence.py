# Date 31/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/longest-increasing-subsequence/
#
############### Longest Increasing Subsequence ###############
# Given an unsorted array of integers, find the length of longest increasing subsequence.
# 
# Example:
# 
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
# 
# Note:
# 
#     There may be more than one LIS combination, it is only necessary for you to return the length.
#     Your algorithm should run in O(n^2) complexity.
# 
# Follow up: Could you improve it to O(n logn) time complexity?
#
# Compexity Analysis
# Time Complexity: O(n^2) and O(n logn)
# Space Complexity: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        N = len(nums)
        dp, longest = [1] * N, 1
        for j in range(1, N):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)
            longest = max(longest, dp[j])
        return longest

    def lengthOfLIS_v2(self, nums: List[int]) -> int:
        if not nums: return 0
        tails = [0] * len(nums)
        size = 0
        for num in nums:
            l, r = 0, size
            while l != r:
                m = (l + r) // 2
                if tails[m] < num:
                    l = m + 1
                else:
                    r = m
            tails[i] = num
            size = max(l + 1, size)
        return size
        
def main():
    sol = Solution()
    nums = [10,9,2,5,3,7,101,18]
    print(sol.lengthOfLIS(nums))
    
if __name__ == "__main__":
    main()
