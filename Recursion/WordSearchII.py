# Date 29/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/word-search-ii/
#
############### Word Search II ###############
# Given a 2D board and a list of words from the dictionary, find all words in the board.
#  Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or 
# vertically neighboring. The same letter cell may not be used more than once in a word.
# 
# Example:
# Input: board = [
#                  ['o','a','a','n'],
#                  ['e','t','a','e'],
#                  ['i','h','k','r'],
#                  ['i','f','l','v']
#                ]
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#  
# Note:
#     All inputs are consist of lowercase letters a-z.
#     The values of words are distinct.

import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not words or not board: return []
        res = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.root, i, j, '', res, dirs)
        return res
        
    def dfs(self, board, node, i, j, path, res, dirs):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node: return
        board[i][j] = '#'
        for d in dirs:
            self.dfs(board, node, i + d[0], j + d[1], path + tmp, res, dirs)
        board[i][j] = tmp        
        
def main():
    sol = Solution()
    board = [ ['o','a','a','n'], ['e','t','a','e'], ['i','h','k','r'], ['i','f','l','v'] ]
    words = ["oath","pea","eat","rain"]
    print(sol.findWords(board, words)) 
    
if __name__ == "__main__":
    main()
