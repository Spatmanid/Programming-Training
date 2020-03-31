# Date 31/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/coin-change/
#
############### Coin Change ###############
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest 
# number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the 
# coins, return -1.
#
# Example 1:
# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# 
# Example 2:
# Input: coins = [2], amount = 3
# Output: -1
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.
#
# Complexity Analysis
# Time: O(N * C), where N = # of different coins and C is the amount you want to make up.
# Space: O(C).

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [0] + [float('inf')] * amount
        for c in coins:
            for j in range(c, amount+1):
                dp[j] = min(dp[j], dp[j-c] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1
        
def main():
    sol = Solution()
    coins, amount = [1, 2, 5], 11
    print(sol.coinChange(coins, amount))
    coins, amount = [2], 3
    print(sol.coinChange(coins, amount))
    
if __name__ == "__main__":
    main()
