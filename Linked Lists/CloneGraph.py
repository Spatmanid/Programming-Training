# Date 24/03/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/clone-graph/
#
############### Clone Graph ###############
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
#
# class Node {
#    public int val;
#    public List<Node> neighbors;
# }
#
# Constraints:
#     1 <= Node.val <= 100
#     Node.val is unique for each node.
#     Number of Nodes will not exceed 100.
#     There is no repeated edges and no self-loops in the graph.
#     The Graph is connected and all nodes can be visited starting from the given node.

class Solution:
    def cloneGraph(self, node):
        memory = {}
        def clone(node):
            if node not in memory:
                c = memory[node] = Node(node.val, None)
                c.neighbors = list(map(clone, node.neightbors))
            return memory[node]
        return node and clone(node)
