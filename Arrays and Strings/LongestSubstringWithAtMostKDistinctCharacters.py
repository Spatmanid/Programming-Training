# Date 25/02/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
#
############### Longest substring with at most two distinct characters ###############
# Given a string s , find the length of the longest substring t that contains at most k distinct characters.
#
# Example 1:
# Input: "eceba", k = 2
# Output: 3
# Explanation: t is "ece" which its length is 3.
# 
# Example 2:
# Input: "ccaabbb", k = 1
# Output: 3
# Explanation: t is "bbb" which its length is 3.
#
# Solution
# Perform a sliding window keeping the loop invariant that l will be the smallest index for which [l, r] is a valid substring.
# Maintain a hashmap where we keep the index of the last position we spotted r.
#
# Complexity Analysis
# Time Complexity: O(N). Index r will iterate N times.
# Space Complexity: O(k). The dictionary will have at most k items.

class Solution:
    def longestSub(self, s, k) -> int:
        if len(s) <= k: return len(s)
        hashMap = {}
        l = r = longest = 0
        while r < len(s):
            if len(hashMap) <= k:
                hashMap[s[r]] = r
                r += 1
            if len(hashMap) > k:
                x = min(hashMap, key = lambda i: hashMap[i])
                l = hashMap[x] + 1
                del hashMap[x]
            longest = max(longest, r - l)
        return longest
        
def main():
    sol = Solution()
    s, k = "eceba", 2
    print(sol.longestSub(s, k))
    s, k = "ccaabbb", 1
    print(sol.longestSub(s, k))
    
if __name__ == "__main__":
    main()
