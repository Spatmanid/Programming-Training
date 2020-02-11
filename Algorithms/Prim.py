# Date 11/02/2020
# @author Spyros Patmanidis
#
#
# Prim's Algorithm
#
# Prim's algorithm is a greedy algorithm that finds a minimum spanning tree 
# for a weighted undirected graph. The idea is to maintain two sets of vertices.
# The first set contains the vertices already included in the MST, the other set 
# contains the vertices not yet included. At every step, it considers all the edges 
# that connect the two sets, and picks the minimum weight edge from these edges. 
# After picking the edge, it moves the other endpoint of the edge to the set containing 
# MST. A group of edges that connects two set of vertices in a graph is called cut in 
# graph theory. So, at every step of Prim’s algorithm, we find a cut (of two sets, one 
# contains the vertices already included in MST and other contains rest of the verices), 
# pick the minimum weight edge from the cut and include this vertex to MST Set (the set 
# that contains already included vertices).
#
# Complexity analysis
# If the input graph is represented using adjacency matrix, Prim's algorithm complexity is O(V^2). 
# If the input graph is represented using adjacency list, then the time complexity of Prim’s 
# algorithm can be reduced to O(E logV) with the help of binary heap.

import collections, heapq
class Prim:
    def adjMatrix(self, adjMatrix):
        self.graph = collections.defaultdict(list)
        self.vertices = set()
        for i in range(len(adjMatrix)-1):
            for j in range(1, len(adjMatrix[0])):
                if adjMatrix[i][j] > 0:
                    self.addEdge(str(i), str(j), adjMatrix[i][j])
                self.vertices.add(str(i))
                self.vertices.add(str(j))
                
    def adjList(self, adjList):
        self.graph = collections.defaultdict(list)
        self.vertices = set()
        for u, v, w in adjList:
            self.addEdge(str(u), str(v), w)
            self.vertices.add(str(u))
            self.vertices.add(str(v))
            
    def addEdge(self, u, v, w):
        self.graph[u].append((v, int(w)))
        self.graph[v].append((u, int(w)))
            
    def printResult(self, res):
        print('Minimum spanning Tree')
        print(f"Edge \t // \t Weight")
        for r, w in res:
            print(f"{r} \t // \t {w}")
            
    def primMST(self, start):
        pq = []                         # list of entries arranged in a heap
        entry_finder = {}               # mapping of tasks to entries
        REMOVED = '<removed>'           # placeholder for a removed task
        cur_Best = {}
        V_E = {}
        included = set()
        res = []
        
        def add_Edge(vertex, priority):
            if vertex in entry_finder:
                remove_Edge(vertex)
            entry = [priority, vertex]
            entry_finder[vertex] = entry
            heapq.heappush(pq, entry)
            
        def remove_Edge(vertex):
            entry = entry_finder.pop(vertex)
            entry[-1] = REMOVED
            
        def pop_Edge():
            while pq:
                priority, vertex = heapq.heappop(pq)
                if vertex is not REMOVED:
                    del entry_finder[vertex]
                    return vertex
            if not pq:
                return None
                
        for v in self.vertices:
            add_Edge(v, float('inf'))
            cur_Best[v] = float('inf')
            
        add_Edge(start, 0)
        cur_Best[start] = 0
        included.add(start)
        node = pop_Edge()
        
        while True:
            for v, w in self.graph[node]:
                if v not in included and w < cur_Best[v]:
                    add_Edge(v, w)
                    cur_Best[v] = w
                    V_E[v] = (str(node) + '--' + str(v), cur_Best[v])
            node = pop_Edge()
            included.add(node)
            if not node:
                break
            res.append(V_E[node])
            
        return res
        
def main():
    pr = Prim()
    
    adjMatr = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5], 
               [0, 3, 0, 0, 7], 
               [6, 8, 0, 0, 9], 
               [0, 5, 7, 9, 0]]
    pr.adjMatrix(adjMatr)
    res = pr.primMST('0')
    pr.printResult(res)

    adjLis = [[0,1,2], [0,3,6], [1,2,3], [1,3,8], [1,4,5], [2,4,7], [3,4,9]]
    pr.adjList(adjLis)
    res = pr.primMST('0')
    pr.printResult(res)

    adjLis2 = [['a','d','1'],['a','b','3'],['d','b','3'],['d','c','1'],
               ['d','e','6'],['b','c','1'],['c','e','5'],['c','f','4'],['e','f','2']]
    pr.adjList(adjLis2)
    res = pr.primMST('a')
    pr.printResult(res)
    
if __name__ == "__main__":
    main()
