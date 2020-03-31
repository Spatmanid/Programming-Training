# Date 31/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
############### Best Time to Buy and Sell Stock ###############
# Say you have an array for which the i-th element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an
# algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
#
# Example 2:
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
        curMin, profit = prices[0], 0
        for p in prices[1:]:
            curMin = min(curMin, p)
            profit = max(profit, p - curMin)
        return profit
        
def main():
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))
    prices = [7,6,4,3,1]
    print(sol.maxProfit(prices))
    
if __name__ == "__main__":
    main()
