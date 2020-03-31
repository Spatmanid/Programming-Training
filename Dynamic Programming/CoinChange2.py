# Date 31/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/coin-change/
#
############### Coin Change 2 ###############
# You are given coins of different denominations and a total amount of money. Write a function to compute the number of 
# combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
#
# Example 1:
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#
# Example 2:
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# 
# Example 3:
# Input: amount = 10, coins = [10] 
# Output: 1
#
# Note:
#   You can assume that:
#       0 <= amount <= 5000
#       1 <= coin <= 5000
#       the number of coins is less than 500
#       the answer is guaranteed to fit into signed 32-bit integer
#
# Complexity Analysis
# Time: O(N * C), where N = # of different coins and C is the amount you want to make up.
# Space: O(C).

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0: return 1
        dp = [1] + [0] * amount
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] += dp[j-coin]
        return dp[amount]
        
def main():
    sol = Solution()
    amount, coins = 5, [1, 2, 5]
    print(sol.change(amount, coins))
    amount, coins = 3, [2]
    print(sol.change(amount, coins))
    amount, coins = 10, [10]
    print(sol.change(amount, coins))
    
if __name__ == "__main__":
    main()
