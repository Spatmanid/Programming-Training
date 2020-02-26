# Date 26/02/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/meeting-rooms/
#
############### Meeting Rooms ###############
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a
# person could attend all meetings.
#
# Example 1:
# Input: [[0,30],[5,10],[15,20]]
# Output: false
#
# Example 2:
# Input: [[7,10],[2,4]]
# Output: true
#
# Solution:
# Sort the intervals in ascending order based on their start time.
# For each meeting time examine if the current meeting starts after the previous one.
# If any meeting has to start before the previous meeting return False.
#
# Complexity Analysis
# Time Complexity: O(N logN).
# Space Complexity: O(1).

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals: return True
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
        
def main():
    sol = Solution()
    intervals = [[0,30],[5,10],[15,20]]
    print(sol.canAttendMeetings(intervals))
    intervals = [[7,10],[2,4]]
    print(sol.canAttendMeetings(intervals))
    
if __name__ == "__main__":
    main()
