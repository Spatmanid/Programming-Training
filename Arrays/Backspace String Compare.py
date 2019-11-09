# Backspace String Compare
# You are given two strings S and T. Return if they are equal when both are
# typed into empty text editors. # means a backspace character.

# Examples

# Input: S = 'a#bcd#', T = 'aa#bc'
# Output: False
# Explanation: S will become 'bc' and T will become 'abc'

# Input: S = 'aa#bcd#', T = 'a#abce#d#g#'
# Output: True
# Explanation: Both will become 'abc'

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
