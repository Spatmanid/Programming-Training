# Date 31/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
#
############### Best Time to Buy and Sell Stock IV ###############
# Say you have an array for which the i-th element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
# Note:
#   You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# Example 1:
# Input: [2,4,1], k = 2
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# 
# Example 2:
# 
# Input: [3,2,6,5,0,3], k = 2
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
#              Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#
# Complexity Analysis
# Time: O(N*k), where N = # of days.
# Space: O(N*k). can further improve the bottom-up DP solution to have O(N) space complexity.

class Solution:
    # The following solutions get TLE or MLE
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or not k: return 0
        N = len(prices)
        dp = [[0] * N for i in range(k+1)]
        for i in range(1, k+1):
            maxDiff = -prices[0]
            for j in range(1, N):
                dp[i][j] = max(dp[i][j-1], prices[j] + maxDiff)
                maxDiff = max(maxDiff, dp[i-1][j] - prices[j]) 
        return dp[k][N-1]
    
    # The following solutions get TLE or MLE
    def maxProfitLinearSpace(self, k: int, prices: List[int]) -> int:
        if not prices or not k: return 0
        N = len(prices)
        dp = [0] * N
        prev = [0] * N
        for i in range(1, k+1):
            maxDiff = -prices[0]
            for j in range(1, N):
                dp[j] = max(dp[j-1], prices[j] + maxDiff)
                maxDiff = max(maxDiff, prev[j] - prices[j])
            for j in range(1, N):
                prev[j] = dp[j] 
        return dp[N-1]
        
    # The following solution passes
    def maxProfitPassing(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        N = len(prices)
        if k >= N // 2:
            return sum(x - y for x, y in zip(prices[1:], prices[:-1]) if x > y)
        profits = [0] * n
        for j in range(k):
            # Update new_profits
            max_all = max_prev = max_here = 0
            for i in range(1, n):
                profit = prices[i] - prices[i-1]
                max_here = max(max_here + profit, max_prev + profit, max_prev)
                max_prev = profits[i]
                profits[i] = max_all = max(max_all, max_here)
        return profits[-1]
        
def main():
    sol = Solution()
    prices, k = [2,4,1], 2
    print(sol.maxProfit(prices))
    prices, k = [3,2,6,5,0,3], 2
    print(sol.maxProfit(prices))
    
if __name__ == "__main__":
    main()
