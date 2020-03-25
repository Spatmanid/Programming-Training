# Date 25/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/merge-two-sorted-lists/
#
############### Merge Two Sorted Lists ###############
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the
# first two lists.
#
# Example 1:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
# Complexity Analysis
# Time Complexity: O(max(m, n)), where m is the length of l1 and n is the length of l2.
# Space Complexity: O(1).

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        if not l1:
            point.next = l2
        if not l2:
            point.next = l1
        return head.next
            
        
def main():
    sol = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l = sol.mergeTwoLists(l1, l2)
    res = ''
    res += str(l.val)
    l = l.next
    while l:
        res += '->' + str(l.val)
        l = l.next
    print(res)
    
if __name__ == "__main__":
    main()
