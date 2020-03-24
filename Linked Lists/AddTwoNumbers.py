# Date 24/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/add-two-numbers/
#
############### Add Two Numbers ###############
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and 
# each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example 1:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
# Complexity Analysis
# Time Complexity: O(max(m, n)), where m is the length of l1 and n is the length of l2.
# Space Complexity: O(max(m, n)). The length of the new list is at most max⁡(m,n) + 1.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = point = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            point.next = ListNode(carry % 10)
            point = point.next
            carry //= 10
        return head.next
        
def main():
    sol = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l = sol.addTwoNumbers(l1, l2)
    res = ''
    res += str(l.val)
    l = l.next
    while l:
        res += '->' + str(l.val)
        l = l.next
    print(res)
    
if __name__ == "__main__":
    main()
