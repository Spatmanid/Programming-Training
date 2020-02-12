# Date 12/02/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/odd-even-jump/
#
############### Odd Even Jump ###############
# You are given an integer array A.  From some starting index, you can make a series of jumps.  The (1st, 3rd, 5th, ...) jumps  # in the series are called odd numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even numbered jumps.
# You may from index i jump forward to index j (with i < j) in the following way:
# - During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that A[i] <= A[j] and A[j] is the smallest #   possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
# - During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that A[i] >= A[j] and A[j] is the largest #   possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
# - It may be the case that for some index i, there are no legal jumps.
# A starting index is good if, starting from that index, you can reach the end of the array (index A.length - 1) by jumping some # number of times (possibly 0 or more than once.)
# Return the number of good starting indexes.
#
# Example 1:
# Input: [10,13,12,14,15]
# Output: 2
# Explanation: 
# From starting index i = 0, we can jump to i = 2 (since A[2] is the smallest among A[1], A[2], A[3], A[4] that is greater or 
# equal to A[0]), then we can't jump any more.
# From starting index i = 1 and i = 2, we can jump to i = 3, then we can't jump any more.
# From starting index i = 3, we can jump to i = 4, so we've reached the end.
# From starting index i = 4, we've reached the end already.
# In total, there are 2 different starting indexes (i = 3, i = 4) where we can reach the end with some number of jumps.
#
# Example 2:
# Input: [2,3,1,1,4]
# Output: 3
# Explanation: 
# From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:
# During our 1st jump (odd numbered), we first jump to i = 1 because A[1] is the smallest value in (A[1], A[2], A[3], A[4]) that # is greater than or equal to A[0].
# During our 2nd jump (even numbered), we jump from i = 1 to i = 2 because A[2] is the largest value in (A[2], A[3], A[4]) that # is less than or equal to A[1].  A[3] is also the largest value, but 2 is a smaller index, so we can only jump to i = 2 and not # i = 3.
# During our 3rd jump (odd numbered), we jump from i = 2 to i = 3 because A[3] is the smallest value in (A[3], A[4]) that is 
# greater than or equal to A[2].
# We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.
# In a similar manner, we can deduce that:
# From starting index i = 1, we jump to i = 4, so we reach the end.
# From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
# From starting index i = 3, we jump to i = 4, so we reach the end.
# From starting index i = 4, we are already at the end.
# In total, there are 3 different starting indexes (i = 1, i = 3, i = 4) where we can reach the end with some number of jumps.
#
# Example 3:
# Input: [5,1,3,4,2]
# Output: 3
# Explanation: 
# We can reach the end from starting indexes 1, 2, and 4.
#
# Note:
#    1 <= A.length <= 20000
#    0 <= A[i] < 100000
#
# Solution
# Notice that where you jump to is determined by the state of the current index and the jump number parity.
# For each state you can either jump to exactly one state or you cannot jump at all. If we find a way to determine these jumps, 
# the problem can be solved with a simple traversal.
# Assume that we are on an odd-numbered jump. Consider the values of A in order from the smallest to largest. When we consider a # value A[j], we search the values we have already processed (which are smaller or equal to A[j]) from largest to smallest. If 
# we find an already processed value A[i] with i<j, then we know that from i we should jump to j. In order to do this 
# efficiently we can use a monotonic stack. We store the indices i of the processed values in a stack and we maintain the 
# invariant that is monotone decreasing. When we ass a new index j, we pop all the smaller indices i<j from the stack, which all # jump to j.
# So, we can determine next_higher[i] which is the index where i jumps to if it is an odd-numbered jump. Similarly, we can 
# determine next_lower[i]. 
# 
# Complexity Analysis
# Time Complexity: O(Nlog⁡N), where N is the length of A.
# Space Complexity: O(N).

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)
        next_higher, next_lower = [0] * N, [0] * N
        
        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)
            
        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)
            
        higher, lower = [0] * N, [0] * N
        higher[-1] = lower[-1] = 1
        for i in range(N-1)[::-1]:
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
        return sum(higher)

def main():
    sol = Solution()
    A = [10,13,12,14,15]
    print(sol.oddEvenJumps(A))
    A = [2,3,1,1,4]
    print(sol.oddEvenJumps(A))
    A = [5,1,3,4,2]
    print(sol.oddEvenJumps(A))
    
if __name__ == "__main__":
    main()
