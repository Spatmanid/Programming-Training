# 25/11/2019
# @author Spyros Patmanidis
#
#
# A* Algorithm
#
# A* algorithm is a graph traversal and path search algorithm, which is 
# often used in computer science due to its completeness, optimality, 
# and optimal efficiency.
#
# Complexity analysis
# The time complexity of the algorithm is O(E) and the space complexity 
# is O(V), where V is the number of vertices and E is the number of edges.

import collections
import heapq

class Solution:
    def __init__(self):
        self.graph = collections.defaultdict(list)
        self.vertices = set()
        self.heuristic = dict()
        
    def createGraph(self, edges, heuristic):
        for u, v, d in edges:
            self.graph[u].append((v, int(d)))
            self.graph[v].append((u, int(d)))
            self.vertices.add(u)
            self.vertices.add(v)
        for v in heuristic:
            self.heuristic[v] = heuristic[v]
    
    def aStar(self, start, end):
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
            
        addDestination(start, None, 0 + self.heuristic[start])
        curBest[start] = 0
        node, origin = popDestination()
        
        while node != end:
            for v, d in self.graph[node]:
                newDistance = curBest[node] + d
                if newDistance < curBest[v]:
                    curBest[v] = newDistance
                    addDestination(v, node, newDistance + self.heuristic[v])
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
    heuristic = {'a':0, 'b':1, 'c':2, 'd':1, 'e':2}
    sol.createGraph(edges, heuristic)
    sol.aStar('a', 'e')
    
if __name__ == "__main__":
    main()
