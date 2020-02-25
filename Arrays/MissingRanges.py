# Date 25/02/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/missing-ranges/
#
############### Missing Ranges ###############
# Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing
# ranges.
#
# Example:
# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]
#
# Complexity Analysis
# Time Complexity: O(n), where m is the length of num1 and n is the length of num2.
# Space Complexity: O(1).

class Solution:
    def findMissingRanges(self, nums, lower, upper):
        nums.insert(0, lower-1)
        nums.append(upper+1)
        missing = []
        for i in range(len(nums)-1):
            if nums[i] + 1 < nums[i+1]:
                if nums[i] + 2 == nums[i+1]:
                    missing.append(str(nums[i] + 1))
                else:
                    missing.append(str(nums[i] + 1) + '->' + str(nums[i+1] - 1))
        return missing

def main():
    sol = Solution()
    nums, lower, upper = [0, 1, 3, 50, 75], 0, 99
    print(sol.findMissingRanges(nums, lower, upper))
    
if __name__ == "__main__":
    main()
