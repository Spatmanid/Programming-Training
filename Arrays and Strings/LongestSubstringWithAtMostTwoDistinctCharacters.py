# Date 25/02/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
#
############### Longest substring with at most two distinct characters ###############
# Given a string s , find the length of the longest substring t that contains at most 2 distinct characters.
#
# Example 1:
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
# 
# Example 2:
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.
#
# Solution
# Perform a sliding window keeping the loop invariant that l will be the smallest index for which [l, r] is a valid subarray.
# Maintain a hashmap where we keep the index of the last position we spotted r.
#
# Complexity Analysis
# Time Complexity: O(N). Index r will iterate N times.
# Space Complexity: O(1).

class Solution:
    def longestSub(self, s) -> int:
        if len(s) <= 2: return len(s)
        hashMap = {}
        l = r = longest = 0
        while r < len(s):
            if len(hashMap) <= 2:
                hashMap[s[r]] = r
                r += 1
            if len(hashMap) > 2:
                x = min(hashMap, key=lambda i:hashMap[i])
                l = hashMap[x] + 1
                del hashMap[x]
            longest = max(longest, r - l)
        return longest
        
def main():
    sol = Solution()
    s = "eceba"
    print(sol.longestSub(s))
    s = "ccaabbb"
    print(sol.longestSub(s))
    
if __name__ == "__main__":
    main()
