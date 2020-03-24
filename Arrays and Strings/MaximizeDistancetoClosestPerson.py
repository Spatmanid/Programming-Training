# Date 24/03/2020
# @author Spyros Patmanidis
#
#
# References
# https://leetcode.com/problems/maximize-distance-to-closest-person/
#
#
############### Maximize Distance to Closest Person Easys ###############
# In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 
# There is at least one empty seat, and at least one person sitting.
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
# Return that maximum distance to closest person.
#
# Example 1:
# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
#
# Example 2:
# Input: [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
#
# Note: 
#    1 <= seats.length <= 20000
#    seats contains only 0s or 1s, at least one 0, and at least one 1.
#
# Solution:
# In a group of k adjacent empty seats, the maximum distance between two people is (k+1) div 2.
# Corner case: the distance of a person for the edge of a row.
#
# Complexity Analysis
# Time Complexity: O(N).
# Space Complexity: O(N).

import itertools
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxDist = 0
        for seat, group in itertools.groupby(seats):
            if not seat:
                k = len(list(group))
                maxDist = max(maxDist, (k+1) // 2)
        return max(maxDist, seats.index(1), seats[::-1].index(1))
        
def main():
    sol = Solution()
    seats = [1,0,0,0,1,0,1]
    print(sol.maxDistToClosest(seats))
    seats = [1,0,0,0]
    print(sol.maxDistToClosest(seats))

if __name__ == "__main__":
    main()
