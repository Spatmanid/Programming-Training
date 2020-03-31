# Date 31/03/2020
# @author Spyros Patmanidis
#
# References
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
#
############### 0-1 Knapsack Problem ###############
# Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the 
# knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated
# with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of 
# val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the
# complete item, or don’t pick it (0-1 property).
#
# Example
# Input: val = [60, 100, 120]
#         wt = [10, 20, 30]
#         W = 50
# Output: 220
#
# Complexity Analysis
# Time: O(N * W), where N = # of items and C = knapsack capacity.
# Space: O(N * C). We can further improve our bottom-up DP solution to have O(C) space complexity.

class Solution:
    def knapsack(self, val, wt, W):
        N = len(val)
        if W <= 0 or N == 0 or len(wt) != N: return 0
        dp = [ [0] * (W + 1) for _ in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, W+1):
                if wt[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], val[i-1] + dp[i-1][j - wt[i-1]])
        return dp[N][W]
        
    def knapsack_v2(self, val, wt, W):
        # O(C) space complexity solution
        N = len(val)
        if W <= 0 or N == 0 or len(wt) != N: return 0
        dp = [ [0] * (W + 1) for _ in range(2)]
        for i in range(1, N+1):
            for j in range(1, W+1):
                if wt[i-1] > j:
                    dp[i%2][j] = dp[(i-1)%2][j]
                else:
                    dp[i%2][j] = max(dp[(i-1)%2][j], val[i-1] + dp[(i-1)%2][j - wt[i-1]])
        return dp[N%2][W]

def main():
    sol = Solution()
    val, wt, W = [60, 100, 120], [10, 20, 30], 50
    print(sol.knapsack(val, wt, W))
    print(sol.knapsack_v2(val, wt, W))
    
if __name__ == "__main__":
    main()
