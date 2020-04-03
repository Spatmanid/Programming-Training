# Date 03/04/2020
# @author Spyros Patmanidis
#
# References
# https://www.geeksforgeeks.org/cutting-a-rod-dp-13/
#
############### Cutting a Rod ###############
# Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine
# the maximum value obtainable by cutting up the rod and selling the pieces. For example, if length of the rod is 8 and the 
# values of different pieces are given as following, then the maximum obtainable value is 22 (by cutting in two pieces of 
# lengths 2 and 6) 
# 
# length   | 1   2   3   4   5   6   7   8  
# -----------------------------------------
# price    | 1   5   8   9  10  17  17  20
#
# And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1)
# 
# length   | 1   2   3   4   5   6   7   8  
# -----------------------------------------
# price    | 3   5   8   9  10  17  17  20
#
# Complexity Analysis
# Time: O(n^2).
# Space: O(n).

class Solution:
    def rodCutting(self, price):
        n = len(price)
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            max_val = -1
            for j in range(i):
                max_val = max(max_val, price[j] + dp[i-j-1])
            dp[i] = max_val
        return dp[n]

def main():
    sol = Solution()
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    print(f"The Maximum obtainable value is {sol.rodCutting(price)}")
    price = [3, 5, 8, 9, 10, 17, 17, 20]
    print(f"The Maximum obtainable value is {sol.rodCutting(price)}")

if __name__ == "__main__":
    main()
