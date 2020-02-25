# Date 13/11/2019
# @author Spyros Patmanidis
#
#
# References
# https://leetcode.com/problems/expressive-words/
#
#
# Expressive Words
#
# Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo",
# "hi" -> "hiiii". In these strings like "heeellooo", we have groups of adjacent letters that 
# are all the same: "h", "eee", "ll", "ooo".
# 
# For some given string S, a query word is stretchy if it can be made to be equal to S by any 
# number of applications of the following extension operation: choose a group consisting of 
# characters c, and add some number of characters c to the group so that the size of the group 
# is 3 or more.
#
# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo",
# but we cannot get "helloo" since the group "oo" has size less than 3. Also, we could do another 
# extension like "ll" -> "lllll" to get "helllllooo". If S = "helllllooo", then the query word 
# "hello" would be stretchy because of these two extension operations:
# query = "hello" -> "hellooo" -> "helllllooo" = S.
#
# Given a list of query words, return the number of words that are stretchy. 
#
# Examples
#
# Input: S = 'heeellooo', words = ['hello', 'hi', ' helo']
# Output: True
# Explanation: We can extend "e" and "o" in the word "hello" to get "heeellooo". We can't extend 
#              "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
#
# Notes:
#   0 <= len(S) <= 100.
#   0 <= len(words) <= 100.
#   0 <= len(words[i]) <= 100.
#   S and all words in words consist only of lowercase letters.
#
# Solution
#
# In this problem, we use Run Length Encoding. For some word, we write the head character of every
# group and count the characters of this group. For example, for the word 'heeellooo', we write the 
# key 'helo' and the count [1,3,2,3].
#
# To see if a word is streachy, the first thing we need is to have the same key as S. If the two keys
# are the same we compare the individual counts c1 = S.count[i] and c2 = word.count[i].
#
# 1. If c1 < c2, then we cannot make make the ith group of word equal to the ith word of S by adding characters.
# 2. If c1 >= 3, then we can add letters to the ith group of word to match the it group of S, as the latter is extended.
# 3. Else, if c1 < 3, then we must have c1 == c2 for the ith groups of word and S to match.
#
# Complexity Analysis
# This solution has time complexity of O(nK), where n is the length of the array words and K is the maximum length of a word.
# This solution has space complexity of O(K).

from itertools import groupby
class Solution:
    def expressiveWords(self, S, words):
        def RLE(S):
            return zip(*[(k, len(list(grp))) for k, grp in groupby(S)])

        key, count = RLE(S)
        res = 0
        for word in words:
            key_w , count_w = RLE(word)
            if key != key_w: continue
            res += all(c1 >= max(c2,3) or c1 == c2 for c1, c2 in zip(count, count_w))
        return res
        
def main():
    S, words = 'heeellooo', ['hello', 'hi', ' helo']
    sol = Solution()
    print(sol.expressiveWords(S, words))
    
if __name__ == "__main__":
    main()
