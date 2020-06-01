# Date 02/06/2020
# @author Spyros Patmanidis
#
#
# Tarjan's Algorithm Algorithm
#
# Tarjan's algorithm is an algorithm in graph theory for finding the strongly connected components 
# of a directed graph. It runs in linear time, matching the time bound for alternative methods 
# including Kosaraju's algorithm and the path-based strong component algorithm.
#
# Complexity analysis
# The time complexity for this algorithm for a graph represented using adjacency list is O(𝑉+𝐸).

import collections

class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list)
        self.vertices = set()
    
    def createGraph(self, edges):
        for u, v in edges:
            self.graph[u].append(v)
            self.vertices.add(u)
            self.vertices.add(v)
            
    def tarjans(self):
        stackMember = set()
        stack = []
        disc = [-1] * len(self.vertices)
        low = [-1] * len(self.vertices)
        self.time = 0
        self.res = []
        
        for v in self.vertices:
            if disc[v] == -1:
                self.tarjansUtil(v, stack, stackMember, disc, low)
                
        print(self.res)
    
    def tarjansUtil(self, u, stack, stackMember, disc, low):
        stackMember.add(u)
        stack.append(u)
        disc[u] = low[u] = self.time
        self.time += 1
        
        for v in self.graph[u]:
            if disc[v] == -1:
                self.tarjansUtil(v, stack, stackMember, disc, low)
                low[u] = min(low[u], low[v])
            elif v in stackMember:
                low[u] = min(low[u], disc[v])
                
        top = -1
        cc = ''
        if low[u] == disc[u]:
            while top != u:
                top = stack.pop()
                stackMember.remove(top)
                cc = str(top) + '-' + cc
            self.res.append(cc.rstrip('-'))
        
def main():
    edges = [[0,1], [1,2], [2,0], [1,3], [3,4], [4,5], [5,3], [6,5], [6,7], [7,8], [8,9], [9,6], [9,10]]
    g = Graph()
    g.createGraph(edges)
    g.tarjans()
    
if __name__ == "__main__":
    main()
