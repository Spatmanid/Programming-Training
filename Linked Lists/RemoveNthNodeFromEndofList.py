# Date 25/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#
############### Remove Nth Node From End of List ###############
# Given a linked list, remove the n-th node from the end of list and return its head.
# 
# Example:
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# 
# Note:
#   Given n will always be valid.
# Follow up:
#   Could you do this in one pass?
#
# Complexity Analysis
# Time Complexity: O(m), where m is the length of the list.
# Space Complexity: O(1).

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = first = second = ListNode(0)
        dummy.next = head
        for _ in range(n+1):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
        
def main():
    sol = Solution()
    nodesRev = [5,4,3,2,1]
    head = p = ListNode(0)
    while nodesRev:
        p.next = ListNode(nodesRev.pop())
        p = p.next
    l = sol.removeNthFromEnd(head.next, 2)
    res = ''
    res += str(l.val)
    l = l.next
    while l:
        res += '->' + str(l.val)
        l = l.next
    print(res)
    
if __name__ == "__main__":
    main()
