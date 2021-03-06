# Date 11/02/2020
# @author Spyros Patmanidis
#
#
# Kosaraju's Algorithm Algorithm
#
# Kosaraju's algorithm (also known as the Kosaraju–Sharir algorithm) is a 
# linear time algorithm to find the strongly connected components of a 
# directed graph. It makes use of the fact that the transpose graph (the 
# same graph with the direction of every edge reversed) has exactly the 
# same strongly connected components as the original graph. 
#
# Complexity analysis
# Provided the graph is described using an adjacency list, Kosaraju's algorithm 
# performs two complete traversals of the graph and so runs in O(V + E) (linear) time.
# If the graph is represented as an adjacency matrix, the algorithm requires O(V^2) time.

import collections, random
class Kosaraju:
    def __init__(self):
        self.graph = collections.defaultdict(list)
        self.revgr = collections.defaultdict(list)
        self.V = set()
        
    def createGraph(self, edges):
        for u, v in edges:
            self.addEdge(u,v)
            self.V.add(u)
            self.V.add(v)
            
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.revgr[v].append(u)
    
    def kosaraju(self, edges):
        def dfs(node):
            for nei in self.graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
            stack.append(node)
        
        def rev_dfs(node):
            comp.append(str(node))
            for nei in self.revgr[node]:
                if nei not in visited:
                    visited.add(nei)
                    rev_dfs(nei)
        
	self.createGraph(edges)
        stack, res = [], []
	
        visited = set()
        for v in self.vertices:
            if v not in visited:
                dfs(v)
                
        visited = set()
        while stack:
            v = stack.pop()
            comp = []
            if v not in visited:
                visited.add(v)
                rev_dfs(v)
            if comp:
                res.append(''.join(comp))
        
        return res
        
def main():
	kos = Kosaraju()
    edges = [['a','b'], ['b','c'], ['b','d'], ['c','a'], ['d','e'],
        ['e','f'], ['f','d'], ['g','f'], ['g','h'], ['h','i'],
        ['i','j'], ['j','g'], ['j','k']]
	kos.createGraph(edges)
	print(kos.kosaraju())
    edges = [[0,1],[1,2],[2,0],[1,3]]
	kos.createGraph(edges)
	print(kos.kosaraju())
    
if __name__ == "__main__":
    main()
