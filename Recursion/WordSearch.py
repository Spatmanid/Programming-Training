# Date 29/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/word-search/
#
############### Word Search ###############
# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# 
# Constraints:
#    board and word consists only of lowercase and uppercase English letters.
#    1 <= board.length <= 200
#    1 <= board[i].length <= 200
#    1 <= word.length <= 10^3
#
# Complexity Analysis
# Time Complexity: O(m * n * s), where m = # of rows, n = # of cols and s = len(word).
# Space Complexity: O(s).

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word or not board: return False
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, dirs, i, j, 0):
                    return True
        return False
        
    def dfs(self, board, word, dirs, i, j, l):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[l]: return False
        if l == len(word) - 1 and word[l] == board[i][j]:
            return True
        tmp = board[i][j]
        board[i][j] = '#'
        found = any(self.dfs(board, word, dirs, i + d[0], j + d[1], l + 1) for d in dirs)
        board[i][j] = tmp
        return found        
        
def main():
    sol = Solution()
    board = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
    word = 'ABCCED'
    print(sol.exist(board, word))
    board = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
    word = 'SEE'
    print(sol.exist(board, word))
    board = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
    word = 'ABCB'
    print(sol.exist(board, word))
    
    
if __name__ == "__main__":
    main()
