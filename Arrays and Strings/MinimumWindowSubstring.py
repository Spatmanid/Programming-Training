# Date 25/02/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/minimum-window-substring/
#
############### Minimum Window Substring ###############
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# Example:
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# 
# Note:
#     If there is no such window in S that covers all characters in T, return the empty string "".
#     If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
#
# Approach
# 1. Find the first window that contains all letter in T.
# 2. Keep expanding the window to the right by 1 character at a time, reducing the left side if possible. Make sure that the active
#    window always contains all letters in T. In this case, every time the window is expanded, only the new character need to be 
#    checked.
#
# Complexity Analysis
# Time Complexity: O(len(S) + len(T))
# Space Complexity: O(len(S) + len(T))

import collections
class Solution:
    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)
        left = start = end = 0
        for right, c in enumerate(s, 1):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            if not missing:
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if not end or right - left <= end - start:
                    start, end = left, right
                need[s[left]] += 1
                left += 1
                missing += 1
        return s[start:end]
            
def main():
    sol = Solution()
    S, T = "ADOBECODEBANC", "ABC"
    print(sol.minWindow(S, T))
    
if __name__ == "__main__":
    main()
