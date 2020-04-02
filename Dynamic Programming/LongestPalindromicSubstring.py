# Date 31/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/longest-palindromic-substring/
#
############### Longest Palindromic Substring ###############
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
# Example 2:
# 
# Input: "cbbd"
# Output: "bb"
#
# Complexity Analysis
# Time: O(n^2), where n = len(s). Can be done in O(n) time by using Manacher's algorithm.
# Space: O(n^2). Manacher's algorithm needs O(n) additional space.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        N = len(s)
        dp = [[True] * N for _ in range(N)]
        start, longest = 0, 1
        for k in range(2, N):
            for i in range(Ν - k + 1):
                j = i + k - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    if k > longest:
                        longest = k
                        start = i
                else:
                    dp[i][j] = False
        return s[start:start+longest]
    
    def manacher(self, s: str) -> str:
        if not s: return ''
        st = '$'
        for c in s:
            st += c + '$'
        c, r, N = 0, 0, len(st)
        dp = [0] * N
        for i in range(N):
            if r > i:
                dp[i] = min(r-i, dp[2*c - i])
            while (i + 1 + dp[i] < N and i - 1 - dp[i] >= 0 and st[i+1+dp[i]] == st[i-1-dp[i]]):
                dp[i] += 1
            if i + dp[i] > r:
                c = i
                r = i + dp[i]
        c = maxLen = 0
        for i, d, in enumerate(dp):
            if d > maxLen:
                maxLen = d
                c = i
        return st[c-maxLen:c+maxLen+1].replace('$', '')
        
def main():
    sol = Solution()
    s = "babad"
    print(sol.longestPalindrome(s))
    print(sol.manacher(s))
    s = "cbbd"
    print(sol.longestPalindrome(s))
    print(sol.manacher(s))

    
if __name__ == "__main__":
    main()
