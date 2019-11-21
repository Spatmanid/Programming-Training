# 21/11/2019
# @author Spyros Patmanidis
#
#
# Dikstra's Algorithm
#
# Dikstra's algorithm is an algorithm for finding the shorthes path between
# two nodes in a graph.
#
# Complexity analysis
# The time complexity of the algorithm is O(E log V) and the space complexity 
# is O(V), where V is the number of vertices and E is the number of edges.

import collections
import heapq

class Solution:
    def __init__(self):
        self.graph = collections.defaultdict(list)
        self.vertices = set()
        
    def createGraph(self, edges):
        for u, v, d in edges:
            self.graph[u].append((v, int(d)))
            self.graph[v].append((u, int(d)))
            self.vertices.add(u)
            self.vertices.add(v)
    
    def dikstras(self, start, end):
        pq = []                     # list of entries arranged in a heap
        entryFinder = {}            # mapping of tasks to entries
        REMOVED = '<removed>'       # placecholder for a removed task
        curBest = {}
        stack = {}
        
        def addDestination(destination, origin, priority):
            'Add a new task or update the priority of an existing task'
            if destination in entryFinder:
                removeDestination(destination)
            entry = [priority, destination, origin]
            entryFinder[destination] = entry
            heapq.heappush(pq, entry)
            
        def removeDestination(destination):
            'Mark an existing entry as REMOVED.'
            entry = entryFinder.pop(destination)
            entry[-1], entry[-2] = REMOVED, REMOVED
            
        def popDestination():
            'Remove and return the lowest priority destination.'
            while pq:
                _, destination, origin = heapq.heappop(pq)
                if destination is not REMOVED:
                    del entryFinder[destination]
                    return destination, origin
            raise KeyError('pop from an empty priority queue')
            
        for v in self.vertices:
            addDestination(v, None, float('inf'))
            curBest[v] = float('inf')
            
        addDestination(start, None, 0)
        curBest[start] = 0
        node, origin = popDestination()
        
        while node != end:
            for v, d in self.graph[node]:
                newDistance = curBest[node] + d
                if newDistance < curBest[v]:
                    curBest[v] = newDistance
                    addDestination(v, node, newDistance)
            stack[node] = (origin, curBest[node])
            node, origin = popDestination()
        stack[node] = (origin, curBest[node])
        s = []
        while node:
            s.append(node)
            node = stack[node][0]
        
        print('->'.join(s[::-1]))

def main():
    sol = Solution()
    edges = [['a','b','3'], ['a','c','1'], ['b','d','2'], ['c','d','1'], ['c','e','3'], ['d','e','1']]
    sol.createGraph(edges)
    sol.dikstras('a', 'e')
    
if __name__ == "__main__":
    main()
