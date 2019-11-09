# Date 09/11/2019
# @author Spyros Patmanidis
#
#
# References
# https://leetcode.com/problems/backspace-string-compare/
#
#
# Backspace String Compare
#
# You are given two strings S and T. Return if they are equal when both are
# typed into empty text editors. # means a backspace character.
#
# Examples
#
# Input: S = 'a#bcd#', T = 'aa#bc'
# Output: False
# Explanation: S will become 'bc' and T will become 'abc'
#
# Input: S = 'aa#bcd#', T = 'a#abce#d#g#'
# Output: True
# Explanation: Both will become 'abc'
#
# Solution
#
# In this problem, we can traverse each string's character and use a stack in order to store the characters
# we have encountered. When the current characters is '#', instead of appending the character to the stack,
# we check if the stack contains at least one character, and if this condition is true, we pop the character
# at the top of the stack.
#
# Complexity Analysis
# This solution has time complexity of O(m + n), where m, n are the lengths of S and T respectively, and
# space complexity of O(m + n).

def backSpaceCompare(S, T):
	
	def buildString(s):
		stack = []
		for c in s:
			if c != '#':
				stack.append(c)
			elif stack:
				stack.pop()
		return ''.join(stack)
	
	return buildString(S) == buildString(T)

def main():
	S, T = 'aa#bcd#', 'a#abce#d#g#'
	print(backSpaceCompare(S, T))

if __name__ == "__main__":
	main()
