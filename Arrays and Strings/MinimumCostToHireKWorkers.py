# Date 25/02/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
#
############### Minimum Cost to Hire K Workers ###############
# There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].
# Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay them according to 
# the following rules:
#     Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
#     Every worker in the paid group must be paid at least their minimum wage expectation.
# Return the least amount of money needed to form a paid group satisfying the above conditions.
#
# Example 1:
# Input: quality = [10,20,5], wage = [70,50,30], K = 2
# Output: 105.00000
# Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
#
# Example 2:
# Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
# Output: 30.66667
# Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately. 
#
# Note:
#     1 <= K <= N <= 10000, where N = quality.length = wage.length
#     1 <= quality[i] <= 10000
#     1 <= wage[i] <= 10000
#     Answers within 10^-5 of the correct answer will be considered correct.
#
# Approach
# In this problem, at least one worker will be paid their minimum wage expectation. Additionally, every worker has some minimum
# ratio of dollars to quality that they demand.
# The key here is to iterate over the ratio. Let assume that we hire workers with ratio R or lower. Then, we would want to know
# the K workers with the lowest quality, and the sum of that quality. In order to maintain these variables we are going to use
# a heap.
#
# Algorithm
# Maintain a max-heap of quality. Also maintain sumq (the sum of this heap).
# For each worker in order of ratio, we know all currently considered workers that have a lower ratio. We calculate the 
# candidate answer as this ratio times the the sum of the smallest K workers in quality.
# 
# Complexity Analysis
# Time Complexity: O(N logN).
# Space Complexity: O(N).

import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = sorted((w/q, w, q) for q, w in zip(quality, wage))
        cost, team, sumq = float('inf'), [], 0
        for ratio, w, q in workers:
            heapq.heappush(team, -q)
            sumq += q
            if len(team) > K: sumq += heapq.heappop(team)
            if len(team) == K: cost = min(cost, sumq * ratio)
        return cost
        
def main():
    sol = Solution()
    quality, wage, K = [10,20,5], [70,50,30], 2
    print(sol.mincostToHireWorkers(quality, wage, K))
    quality, wage, K = [3,1,10,10,1], [4,8,2,2,7], 3
    print(sol.mincostToHireWorkers(quality, wage, K))
    
if __name__ == "__main__":
    main()
