# Date 03/04/2020
# @author Spyros Patmanidis
#
# References
# https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
#
############### Maximum Product Cutting ###############
# Given a rope of length n meters, cut the rope in different parts of integer lengths in a way that maximizes product of
# lengths of all parts. You must make at least one cut. Assume that the length of rope is more than 2 meters. 
#
# Examples:
# 
# Input: n = 2
# Output: 1 (Maximum obtainable product is 1*1)
# 
# Input: n = 3
# Output: 2 (Maximum obtainable product is 1*2)
# 
# Input: n = 4
# Output: 4 (Maximum obtainable product is 2*2)
# 
# Input: n = 5
# Output: 6 (Maximum obtainable product is 2*3)
# 
# Input: n = 10
# Output: 36 (Maximum obtainable product is 3*3*4)
#
# Complexity Analysis
# Time: O(n^2).
# Space: O(n).

class Solution:
    def maxProd(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            max_val = 0
            end = i // 2 + 1
            for j in range(1, end):
                max_val = max( max_val, j * (i - j), j * dp[i-j])
            dp[i] = max_val
        return dp[n]
        
def main():
    sol = Solution()
    n = 11
    for i in range(2, N):
        print(f"Maximum Product of {i} is {sol.maxProd(i)}")
    
if __name__ == "__main__":
    main()
