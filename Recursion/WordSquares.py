# Date 29/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/word-squares/
#
############### Word Squares ###############
# Given a set of words (without duplicates), find all word squares you can build from them.
# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, # numColumns).
# For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both 
# horizontally and vertically.
# 
#   b a l l
#   a r e a
#   l e a d
#   l a d y
#
# Note:
#   There are at least 1 and at most 1000 words.
#   All words will have the exact same length.
#   Word length is at least 1 and at most 5.
#   Each word contains only lowercase English alphabet a-z.

import collections
class Solution:
    def wordSquares(self, words):
        N = len(words[0])
        pref, res = collections.defaultdict(set), []
        for w in words:
            for i in range(N):
                pref[w[:i+1]].add(w)
        def dfs(i, arr):
            if i == len(arr[0]):
                res.append(arr)
            else:
                for w in pref[''.join(row[i] for row in arr)]:
                    dfs(i+1, arr + [w])
        for w in words:
            dfs(1, [w])
        return res
        
def main():
    sol = Solution()
    words = ["ball","area","lead","lady",'bars','last','lost','aria','rial','sala']
    print(sol.wordSquares(words))
    
if __name__ == "__main__":
    main()
