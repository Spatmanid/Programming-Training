# Date 18/08/2020
# @author Spyros Patmanidis
#
#
# Manacher's Algorithm
#
# Manacher's algorithm can be used to solve the problem of finding a maximum-length
# contiguous substring of a given string that is also a palindrome in linear time.
#
# Time Complexity
# The runtime complexity of Manacher's algorithm is O(𝑛).

class Solution:
    def manacher(self, s):
        if not s: return ''
        st = '#'
        for c in s:
            st += c + '#'
        c, r, N = 0, 0 , len(st)
        dp = [0] * N
        for i in range(1, N):
            if r > i:
                dp[i] = min(r-i, dp[2*c - i])
            while (i + 1 + dp[i] < N and i - 1 - dp[i] >= 0 and 
                   st[i + 1 + dp[i]] == st[i - 1 - dp[i]]):
                dp[i] += 1
            if i + dp[i] > r:
                c = i
                r = i + dp[i]
        maxLen = 0
        center = 0
        for i in range(N):
            if dp[i] > maxLen:
                maxLen = dp[i]
                center = i       
        return st[center-maxLen:center+maxLen+1].replace('#', '')
