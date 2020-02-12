# Date 12/02/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/fruit-into-baskets/
#
############### Fruit Into Baskets ###############
# In a row of trees, the i-th tree produces fruit with type tree[i].
# You start at any tree of your choice, then repeatedly perform the following steps:
#     1. Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
#     2. Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
# Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then 
# back to step 1, then step 2, and so on until you stop.
# You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of 
# fruit each.
# What is the total amount of fruit you can collect with this procedure?
#
# Example 1:
# Input: [1,2,1]
# Output: 3
# Explanation: We can collect [1,2,1].
#
# Example 2:
# Input: [0,1,2,2]
# Output: 3
# Explanation: We can collect [1,2,2].
# If we started at the first tree, we would only collect [0, 1].
#
# Example 3:
# Input: [1,2,3,2,2]
# Output: 4
# Explanation: We can collect [2,3,2,2].
# If we started at the first tree, we would only collect [1, 2].
#
# Example 4:
# Input: [3,3,3,1,2,1,1,2,3,3,4]
# Output: 5
# Explanation: We can collect [1,2,1,1,2].
# If we started at the first tree or the eighth tree, we would only collect 4 fruits.
#
# Note:
#    1. 1 <= tree.length <= 40000
#    2. 0 <= tree[i] < tree.length
#
# Solution
# Perform a sliding window keeping the loop invariant that l will be the smallest index for which [l, r] is a valid subarray.
# Maintain a hashmap where we keep the index of the last position we spotted r.

class Solution:
	def totalFruit(self, tree: List[int]) -> int:
		if tree == None:
			return 0
		elif len(tree) <= 2:
			return len(tree)
		N, K = len(tree), 2
		hashMap, l, r, max_len = {}, 0, 0, 1
		while r < N:
			if len(hashMap) <= K:
				hashMap[tree[r]] = r
				r += 1
			if len(hashMap) > K:
				index = min(hashMap.values())
				l = index + 1
				del hashMap[tree[index]]
			max_len = max(max_len, r - l)
		return max_len
