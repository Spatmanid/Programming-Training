# Date 26/02/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/meeting-rooms-ii/
#
############### Meeting Rooms II ###############
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum
# number of conference rooms required.
#
# Example 1:
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# 
# Example 2:
# Input: [[7,10],[2,4]]
# Output: 1
#
# Complexity Analysis
# Time Complexity: O(N logN).
# Space Complexity: O(N).

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval[0])
            ends.append(interval[1])
        starts.sort()
        ends.sort()
        i = rooms = 0
        for start in starts:
            if start < ends[i]:
                rooms += 1
            else:
                i += 1
        return rooms
        
        
def main():
    sol = Solution()
    intervals = [[0,30],[5,10],[15,20]]
    print(sol.minMeetingRooms(intervals))
    intervals = [[7,10],[2,4]]
    print(sol.minMeetingRooms(intervals))
    
if __name__ == "__main__":
    main()
