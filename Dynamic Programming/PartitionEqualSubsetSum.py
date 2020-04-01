# Date 31/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/partition-equal-subset-sum/
#
############### Partition Equal Subset Sum ###############
# Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that 
# the sum of elements in both subsets is equal.
# 
# Note:
#   Each of the array element will not exceed 100.
#   The array size will not exceed 200.
#
# Example 1:
# Input: [1, 5, 11, 5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# Example 2:
# Input: [1, 2, 3, 5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
#
# Complexity Analysis
# Time: O(N * C), where N = len(nums) and C = sum(nums).
# Space: O(C).

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums: return False
        total = sum(nums)
        if total % 2: return False
        total //= 2
        dp = [True] + [False] * total
        for num in nums:
            for j in range(num, total+1)[::-1]:
                dp[j] = dp[j] or dp[j-num]
        return dp[total]
        
def main():
    sol = Solution()
    nums = [1, 5, 11, 5]
    print(sol.canPartition(nums))
    nums = [1, 2, 3, 5]
    print(sol.canPartition(nums))
    
if __name__ == "__main__":
    main()
