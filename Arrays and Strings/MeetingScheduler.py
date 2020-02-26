# Date 26/02/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/meeting-scheduler/
#
############### Meeting Scheduler ###############
# Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest
# time slot that works for both of them and is of duration duration.
# If there is no common time slot that satisfies the requirements, return an empty array.
# The format of a time slot is an array of two elements [𝑠𝑡𝑎𝑟𝑡,𝑒𝑛𝑑] representing an inclusive time range from start to end.
# It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots
# [𝑠𝑡𝑎𝑟𝑡1,𝑒𝑛𝑑1] and [𝑠𝑡𝑎𝑟𝑡2,𝑒𝑛𝑑2] of the same person, either 𝑠𝑡𝑎𝑟𝑡1>𝑒𝑛𝑑2 or 𝑠𝑡𝑎𝑟𝑡2>𝑒𝑛𝑑1.
#
# Example 1:
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
# Output: [60,68]
# Example 2:
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
# Output: []
# 
# Constraints:
#     1 <= slots1.length, slots2.length <= 10^4
#     slots1[i].length, slots2[i].length == 2
#     slots1[i][0] < slots1[i][1]
#     slots2[i][0] < slots2[i][1]
#     0 <= slots1[i][j], slots2[i][j] <= 10^9
#     1 <= duration <= 10^6 
#
# Complexity Analysis
# Time Complexity: O(N logN), where N = max(len(slots1), len(slots2)).
# Space Complexity: O(N).

import heapq
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[List[int]]:
        h = []
        for slot in slots1:
            heapq.heappush(h, (slot, 1))
        for slot in slots2:
            heapq.heappush(h, (slot, 2))
        prev = heapq.heappop(h)
        while h:
            cur = heapq.heappop(h)
            if (prev[1] != cur[1]) and (cur[0][0] < prev[0][1] and cur[0][1] > prev[0][0] and
                                        min(cur[0][1], prev[0][1]) - max(cur[0][0], prev[0][0]) >= duration):
                return [max(cur[0][0], prev[0][0]), max(cur[0][0], prev[0][0]) + duration]
            prev = cur
        return []
        
def main():
    sol = Solution()
    slots1, slots2, duration = [[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8
    print(sol.minAvailableDuration(slots1, slots2, duration))
    slots1, slots2, duration = [[10,50],[60,120],[140,210]], [[0,15],[60,70]], 12
    print(sol.minAvailableDuration(slots1, slots2, duration))
    
if __name__ == "__main__":
    main()
