# Date 24/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/add-two-numbers-ii/
#
############### Add Two Numbers II ###############
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and 
# each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
# Example:
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
#
# Complexity Analysis
# Time Complexity: O(max(m, n)), where m is the length of l1 and n is the length of l2. Reversing each list can be done in 
# linear time.
# Space Complexity: O(max(m, n)). The length of the new list is at most max⁡(m,n) + 1. The reverse operation need O(1) space.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1, l2 = self.reverseList(l1), self.reverseList(l2)
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
        return self.reverseList(head.next)
        
    def reverseList(self, head):
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev
            
        
def main():
    sol = Solution()
    l1 = ListNode(7)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)
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
