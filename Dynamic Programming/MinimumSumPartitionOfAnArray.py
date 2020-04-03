# Date 03/04/2020
# @author Spyros Patmanidis
#
# References
# https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
#
############### Minimum Sum Partition Of An Array ###############
# Given an array, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is
# minimum.
#
# Example 1:
# Input: [1,6,5,11]
# Output: 1
# Explanation: The 2 subsets are {1,5,6} and {11} with sums being 12 and 11. Hence answer is 1.
#
# Example 2:
# Input: [36,7,46,40]
# Output: 23
# Explanation: The 2 subsets are {7,46} and {36,40} with sums being 53 and 76. Hence answer is 23.
#
# Constraints
#   1 <= size of array <= 50
#   1 <= a[i] <= 50
#
# Complexity Analysis
# Time: O(N * C), where N = len(nums) and C = sum(nums).
# Space: O(C).

class Solution:
    def minSumPartition(self, nums: List[int]) -> bool:
        if not nums: return False
        total = sum(nums)
        half = total // 2
        dp = [True] + [False] * half
        for num in nums:
            for j in range(num, half+1)[::-1]:
                dp[j] = dp[j] or dp[j-num]
        for j in range(0, half+1)[::-1]:
            if dp[j]:
                half = j
                break
        return total - 2 * half
        
def main():
    sol = Solution()
    nums = [1, 6, 5, 11]
    print(sol.minSumPartition(nums))
    nums = [36, 7, 46, 40]
    print(sol.minSumPartition(nums))
    
if __name__ == "__main__":
    main()
