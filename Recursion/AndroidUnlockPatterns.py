# Date 25/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/android-unlock-patterns/
#
############### Android Unlock Patterns ###############
# Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns # of the Android lock screen, which consist of minimum of m keys and maximum n keys.
#
# Rules for a valid pattern:
#   Each pattern must connect at least m keys and at most n keys.
#   All the keys must be distinct.
#   If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have 
#   previously selected in the pattern. No jumps through non selected key is allowed.
#   The order of keys used matters.
#
# Complexity Analysis
# Time Complexity: O((n-1)!), where n the the max length of pattern.
# Space Complexity: O(1).

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        def dfs(i, used):
            if m <= len(used) <= n:
                self.res += 1
            if len(used) < n:
                for ni in range(1,10):
                    if ni in used or ni == i: continue
                    if (i, ni) in between and between[(i,ni)] not in used: continue
                    used.add(ni)
                    dfs(ni, used)
                    used.remove(ni)
        
        self.res = 0
        between = { (1,3):2, (3,1):2, (1,7):4, (7,1):4, (1,9):5, (9,1):5,
                   (3,7):5, (7,3):5, (3,9):6, (9,3):6, (7,9):8, (9,7):8,
                   (2,8):5, (8,2):5, (4,6):5, (6,4):5}
        for i in range(1, 10):
            dfs(i, set([i]))
        return self.res
        
        
def main():
    sol = Solution()
    print(sol.numberOfPatterns(3, 8))
    
if __name__ == "__main__":
    main()
