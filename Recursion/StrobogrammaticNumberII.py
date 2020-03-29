# Date 29/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/strobogrammatic-number/
#
############### Strobogrammatic Number II ###############
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Find all strobogrammatic numbers that are of length = n.
#
# Example:
# Input: n = 2
# Output: ["11","69","88","96"]

class Solution:
    def findStrobogrammatic(self, n:int):
        oddMidCandidates = ['0', '1', '8']
        evenMidCandidates = ['00', '11', '69', '88', '96']
        if n == 1: return oddMidCandidates
        if n == 2: return evenMidCandidates[:-1]
        if n % 2:
            prefixSuffix, midCandidates = self.findStrobogrammatic(n-1), oddMidCandidates
        else:
            prefixSuffix, midCandidates = self.findStrobogrammatic(n-2), evenMidCandidates
        premid = (n - 1) // 2
        return [pf[:premid] + mid + pf[premid:] for pf in prefixSuffix for mid in midCandidates]
        
def main():
    sol = Solution()
    print(sol.findStrobogrammatic(2))
    
if __name__ == "__main__":
    main()
