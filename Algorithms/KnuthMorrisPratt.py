# 21/11/2019
# @author Spyros Patmanidis
#
#
# Knuth-Morris-Pratt Algorithm - KMP
#
# You are given a text and a pattern. Find the starting positions of the
# pattern inside the text.
#
# Example
#
# Input: text = advcsabceefdsabckfld, pattern = abc
# Output: result = [5, 13]
#
# Complexity Analysis
# This algorithm has time complexity of O(m + n) and space complexity of O(n),
# where m is the length of the text and n is the length of the pattern.

class Solution:
    def findPattern(self, text, pattern):
        if not pattern or not text: return []
        i, exists, result = 0, True, []
        lps = [0] * len(pattern)
        self.computeLPS(pattern, lps)
        while exists:
            i, exists = self.KMP(text, pattern, lps, i)
            if exists:
                result.append(i - len(pattern))
        return result
    
    def computeLPS(self, pattern, lps):
        # compute the longest suffix which is also prefix
        i, j = 1, 0
        while i < len(pattern):
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
                
    def KMP(self, text, pattern, lps, i):
        j = 0
        while i < len(text) and j < len(pattern):
            if text[i] == pattern[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
        if j == len(pattern):
            return i, True
        return -1, False
        
def main():
    sol = Solution()
    test = 'advcsabceefdsabckfld'
    pattern = 'abc'
    print(sol.findPattern(text, pattern))
    
if __name__ == "__main__":
    main()
