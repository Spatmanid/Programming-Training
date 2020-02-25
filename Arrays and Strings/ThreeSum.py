# Date 09/11/2019
# @author Spyros Patmanidis
#
#
# References
# https://leetcode.com/problems/3sum/
#
#
# Three Sum
# Medium
# You are given an array nums of n integers. You are asked to find all the unique triplets
# in the array which give the sum of zero. a, b, c in nums such that a + b + c = 0.
#
# Note: The solution must not contain duplicate triplets.
#
# Examples
#
# Input: nums = [-1, 0, 1, 2, -1, 4]
# Output: [[-1,0,1], [-1,-1,2]]
#
# Solution
#
# In this problem, we have an unordered list of integers. The key idea here is to sort the
# array, so that we can easily move around and know how we need to adjust the low and high
# pointers. This will also help us to avoid duplicates, since we can skip numbers that are
# same to their previous number.
# 
# Complexity Analysis
# In this problem we start by sorting the array nums with O(n logn) and then we iterate
# through the nums with O(n^2). So, it is O(n logn + n^2) = O(n^2). The space complexity is
# O(n) because even though we do not use extra space for the computations we might need 
# to store the entire nums array in the result array.

class Solution:
    def threeSum(self, nums):
        result = []
        n = len(nums)
        if n < 3:
             return result     
        nums.sort()
        
        # we do not have to iterate through the last two elements,
        # because two elements cannot form a triplet.
        for i in range(n - 2):
        
            # if the current element is greater than zero, we can break the for loop,
            # since all the elements after the current one will be positive and we 
            # cannot add positive number to zero
            if nums[i] > 0:
                break
            
            # if the current number is same to the previous one, we can move to the next
            # number, because we have already checked this one.
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # at every iteration we start the low pointer from the element after the
            # current i and the high pointer from the last index of the array nums.
            low, high = i + 1, n - 1
            while low < high:
                total = nums[i] + nums[low] + nums[high]
                if total < 0:
                    low += 1
                elif total > 0:
                    high -= 1
                else:
                    result.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low+1]: low += 1
                    while low < high and nums[high] == nums[high-1] : high -= 1
                    low += 1
                    high -= 1
                    
        return result
            
def main():
    nums = [-1, 0, 1, 2, -1, 4]
    sol = Solution()
    print(sol.threeSum(nums))
    
if __name__ == "__main__":
    main()
