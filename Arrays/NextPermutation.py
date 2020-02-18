# Date 12/02/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/fruit-into-baskets/
#
############### Next Permutation ###############
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place and use only constant extra memory.
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
# Solution
# The first step to solve this problem is to identify the longest non-increasing suffix. This suffix is already the highest 
# permutation, so we cannot modify it to get the next permutation. In order to get the next permutation we need to modify the 
# elements to the left of this suffix. We look at the element at the left of the suffix. We call this element pivot. The pivot 
# is necessarily less than the head of the suffix. Next, we swap the pivot with the smallest element in the suffix that is greater
# than the pivot. As a result the prefix is now minimized. Finally, we reverse the suffix. Now we have the next permutation.

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        N = len(nums)
        i = N - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i <= 0:
            nums.reverse()
        else:
            j = N - 1
            while nums[j] <= nums[i-1]:
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
            nums[i:] = reversed(nums[i:])
