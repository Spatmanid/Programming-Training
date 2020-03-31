# Date 31/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
#
############### Best Time to Buy and Sell Stock III ###############
# Say you have an array for which the i-th element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
#
# Example 1:
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#              Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# 
# Example 2:
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
# 
# Example 3:
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
# Complexity Analysis
# Time: O(N), where N = # of days.
# Space: O(1).

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        k, N = 2, len(prices)
        dp = [ [0] * N for _ in range(2)]
        for i in range(1, k+1):
            maxDiff = -prices[0]
            for j in range(1, N):
                dp[i%2][j] = max(dp[i%2][j-1], prices[j] + maxDiff)
                maxDiff = max(maxDiff, dp[(i-1)%2][j] - prices[j])
        return dp[k%2][N-1]
        
def main():
    sol = Solution()
    prices = [3,3,5,0,0,3,1,4]
    print(sol.maxProfit(prices))
    prices = [1,2,3,4,5]
    print(sol.maxProfit(prices))
    prices = [7,6,4,3,1]
    print(sol.maxProfit(prices))
    
if __name__ == "__main__":
    main()
