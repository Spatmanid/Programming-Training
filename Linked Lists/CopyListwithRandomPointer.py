# Date 24/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/copy-list-with-random-pointer/
#
############### Copy List with Random Pointer ###############
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or
# null.
# Return a deep copy of the list.
# The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of 
# [val, random_index] where:
#
#    val: an integer representing Node.val
#    random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to 
#                  any node.
#
# Constraints:
#    -10000 <= Node.val <= 10000
#    Node.random is null or pointing to a node in the linked list.
#    Number of Nodes will not exceed 1000.

class Node(object):
    def __init__(self, x, n, r):
        self.val = x
        self.next = None
        self.random = None

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        d = {}
        p = head
        chead = dummy = Node(-1, None, None)
        while p:
            if p not in d:
                d[p] = Node(p.val, None, None)
            dummy.next = d[p]
            if p.random:
                if p.random not in d:
                    d[p.random] = Node(p.random.val, None, None)
                dummy.next.random = d[p.random]
            dummy = dummy.next
            p = p.next
        return chead.next
