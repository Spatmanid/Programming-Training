# Date 12/02/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/kth-largest-element-in-an-array/
#
############### Kth Largest Element in an Array ###############
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth 
# distinct element.
#
# Example 1:
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
#
# Example 2:
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#
# Solution
# The idea is to initialize a min heap, and add all elements from the array into this heap one by one keeping the size of the
# heap always less or equal to k. That would results in a heap containing k largest elements of the array.
# 
# Complexity Analysis
# Time Complexity: O(Nlog⁡k), where N is the length of the array.
# Space Complexity: O(k).

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = list(nums[:k])
        heapq.heapify(h)
        for i in range(k, len(nums)):
            heapq.heappushpop(h, nums[i])
        return heapq.heappop(h)

def main():
    sol = Solution()
    nums, k = [3,2,1,5,6,4], 2
    print(sol.findKthLargest(nums, k))
    nums, k = [3,2,3,1,2,4,5,5,6], 4
    print(sol.findKthLargest(nums, k))
    
if __name__ == "__main__":
    main()
