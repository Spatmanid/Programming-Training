# Date 03/04/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/split-array-largest-sum/
#
############### Split Array Largest Sum ###############
# Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous
# subarrays. Write an algorithm to minimize the largest sum among these m subarrays.
# 
# Note:
#   If n is the length of array, assume the following constraints are satisfied:
#       1 ≤ n ≤ 1000
#       1 ≤ m ≤ min(50, n)
# 
# Examples:
# 
# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# 
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
#
# Complexity Analysis
# Time: O(n^2).
# Space: O(1).

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def isValid(mid):
            cnt = cur = 0
            for num in nums:
                cur += num
                if cur > mid:
                    cnt += 1
                    if cnt >= m:
                        return False
                    cur = num
            return True
            
        l, h = max(nums), sum(nums)
        while l < h:
            mid = (l + h) // 2
            if isValid(mid):
                h = mid
            else:
                l = mid + 1
        return l
        
def main():
    sol = Solution()
    nums, S = [7,2,5,10,8], 2
    print(sol.findTargetSumWays(nums, m))
    
if __name__ == "__main__":
    main()
