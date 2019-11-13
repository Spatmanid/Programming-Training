# Date 13/11/2019
# @author Spyros Patmanidis
#
#
# References
# https://leetcode.com/problems/k-closest-points-to-origin/
#
#
# K Closest Points to Origin
#
# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
#
# Here, the distance between two points on a plane is the Euclidean distance.
#
# You may return the answer in any order.  The answer is guaranteed to be unique 
# (except for the order that it is in.)
#
# Examples
#
# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation: The distance between (1, 3) and the origin is sqrt(10). The distance between 
#              (-2, 2) and the origin is sqrt(8). Since sqrt(8) < sqrt(10), (-2, 2) is closer
#              to the origin. We only want the closest K = 1 points from the origin, so the 
#              answer is just [[-2,2]].
#
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# Explanation: (The answer [[-2,4],[3,3]] would also be accepted.)
#
# Solution
#
# Approach One: Sorting
# In this problem, we can sort the points by distance, then take the closest K points.
#
# Complexity Analysis
# This solution has time complexity of O(n logn), where n is the length of the array points.
# The space complexity of this solution is O(1) because we can use the python build-in sort 
# function, which does the sorting in place.
#
# Approach Two: Heap
# We can also use a maxHeap data structure. The maxHeap has the property of returning the 
# maximum element in O(1) time. At each iteration we will add a new element in the maxHeap,
# If we keep a maxHeap of size K, we can add new element in O(logK) time and remove the 
# maximum element of the heap. As a result, we can always keep the current K closest points.

# Complexity Analysis
# If we have n points, the time complexity of this approach is O(n logK) and the space complexity
# is O(K).

import heapq
class Solution:
    def kClosestSorting(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
        
    def kClosestHeap(self, points, K):
        h = []
        for x, y in points[:K]:
            heapq.heappush(h, [-(x**2+y**2), x, y])
        for x, y in points[K:]:
            heapq.heappushpop(h, [-(x**2+y**2), x, y])
        return [[x, y] for _, x, y in h[::-1]]
        
    def kClosestHeapPythonic(self, points, K):
        return heapq.nsmallest(K, points, key=lambda p: p[0]**2 + p[1]**2)
        
def main():
    sol = Solution()
    points, K = [[1,3],[-2,2]], 1
    print(sol.kClosestHeap(points, K))
    points, K = [[3,3],[5,-1],[-2,4]], 2
    print(sol.kClosestHeap(points, K))
    
if __name__ == "__main__":
  main()
